from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # the owner of the note
    shared_users = models.ManyToManyField(User, related_name='shared_notes')  # the users with whom the note is shared

    def __str__(self):
        return self.title

class NoteHistory(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='history')
    title = models.CharField(max_length=200)  # new field for title
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Change at {self.timestamp} by {self.user.username}'