# from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
import json

from .models import Note

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

def get_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.user == note.user:  # assuming you have user authentication in place
        return JsonResponse({'title': note.title, 'content': note.content})
    else:
        return JsonResponse({'error': 'You do not have permission to view this note.'}, status=403)