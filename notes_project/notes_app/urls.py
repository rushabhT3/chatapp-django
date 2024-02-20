from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('notes/create/', views.create_note_view, name='create_note'),
    path('notes/<int:id>/', views.NoteView.as_view(), name='note'),
    path('notes/version-history/<int:id>/', views.NoteHistoryView.as_view(), name='note_history'),
    path('notes/share/<int:id>/', views.ShareNoteView.as_view(), name='share_note'),
]
