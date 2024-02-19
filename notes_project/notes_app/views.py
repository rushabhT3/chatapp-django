# from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.core import serializers
import json

from .models import Note, NoteHistory

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if not username or not password or not email:
            return JsonResponse({'status': 'error', 'message': 'Username, password and email are required'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Username is already taken'}, status=400)
        user = User.objects.create_user(username, email, password)
        return JsonResponse({'status': 'success', 'message': 'User created successfully'}, status=201)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'User logged in successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def create_note_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        if not title or not content:
            return JsonResponse({'status': 'error', 'message': 'Title and content are required'}, status=400)
        Note.objects.create(title=title, content=content, user=request.user)
        return JsonResponse({'status': 'success', 'message': 'Note created successfully'}, status=201)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
class NoteView(View):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)
        if request.user == note.user:  # assuming you have user authentication in place
            return JsonResponse({'title': note.title, 'content': note.content})
        else:
            return JsonResponse({'error': 'You do not have permission to view this note.'}, status=403)

    def put(self, request, id):
        note = get_object_or_404(Note, id=id)
        if request.user == note.user or request.user in note.shared_users.all():
            data = json.loads(request.body)  # parse the request body as JSON
            note.title = data['title']  # update the title
            note.content = data['content']  # use the parsed data
            note.save()
            NoteHistory.objects.create(note=note, title=data['title'], content=data['content'], user=request.user)  # include title here
            return JsonResponse({'message': 'Note updated successfully.'})
        else:
            return JsonResponse({'error': 'You do not have permission to edit this note.'}, status=403)

class NoteHistoryView(View):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)
        if request.user == note.user or request.user in note.shared_users.all():
            note_history = NoteHistory.objects.filter(note=note).order_by('-timestamp')
            data = [{'title': nh.title, 'content': nh.content, 'timestamp': nh.timestamp, 'user': nh.user.username} for nh in note_history]
            return JsonResponse({'note_history': data})
        else:
            return JsonResponse({'error': 'You do not have permission to view this note history.'}, status=403)