from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note, NoteHistory

class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='testuser', password='12345')
        Note.objects.create(title='Test Title', content='Test Content', user=User.objects.get(id=1))

    def test_title_content(self):
        note = Note.objects.get(id=1)
        expected_object_name = f'{note.title}'
        self.assertEquals(expected_object_name, 'Test Title')

class NoteHistoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='testuser', password='12345')
        Note.objects.create(title='Test Title', content='Test Content', user=User.objects.get(id=1))
        NoteHistory.objects.create(note=Note.objects.get(id=1), title='Test Title', content='Test Content', user=User.objects.get(id=1))

    def test_note_history(self):
        note_history = NoteHistory.objects.get(id=1)
        expected_object_name = f'Change at {note_history.timestamp} by {note_history.user.username}'
        self.assertEquals(str(note_history), expected_object_name)
