from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import json

from .models import Note, NoteHistory

class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_view(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'password': '12345',
            'email': 'testuser@example.com'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'success', 'message': 'User logged in successfully'})

class CreateNoteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_note_view(self):
        url = reverse('create_note')
        data = {
            'title': 'Test Title',
            'content': 'Test Content'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Title')

class NoteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.test_note = Note.objects.create(title='Test Title', content='Test Content', user=self.test_user)

    def test_get_note_view(self):
        url = reverse('note', kwargs={'id': self.test_note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'title': 'Test Title', 'content': 'Test Content'})

    def test_put_note_view(self):
        url = reverse('note', kwargs={'id': self.test_note.id})
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content'
        }
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.get(id=self.test_note.id).title, 'Updated Title')
        self.assertEqual(NoteHistory.objects.count(), 1)
        self.assertEqual(NoteHistory.objects.get().title, 'Updated Title')

class NoteHistoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.test_note = Note.objects.create(title='Test Title', content='Test Content', user=self.test_user)
        self.test_note_history = NoteHistory.objects.create(note=self.test_note, title='Test Title', content='Test Content', user=self.test_user)

    def test_get_note_history_view(self):
        url = reverse('note_history', kwargs={'id': self.test_note.id})
        response = self.client.get(url)
        timestamp = self.test_note_history.timestamp.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'note_history': [{'title': 'Test Title', 'content': 'Test Content', 'timestamp': timestamp, 'user': 'testuser'}]})

class ShareNoteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user1 = User.objects.create_user(username='testuser1', password='testpassword1')
        self.test_user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        self.client.login(username='testuser1', password='testpassword1')
        self.test_note = Note.objects.create(title='Test Title', content='Test Content', user=self.test_user1)

    def test_share_note_view(self):
        url = reverse('share_note', kwargs={'id': self.test_note.id})
        data = {
            'user_ids': [self.test_user2.id]
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.get(id=self.test_note.id).shared_users.count(), 1)
        self.assertEqual(Note.objects.get(id=self.test_note.id).shared_users.first(), self.test_user2)

