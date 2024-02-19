from django.urls import path
from . import views
# from .views import NoteView
# from .views import create_note_view

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('notes/create/', views.create_note_view, name='create_note'),
    path('notes/<int:id>/', views.NoteView.as_view(), name='note'),
    path('notes/version-history/<int:id>/', views.NoteHistoryView.as_view(), name='note_history'),
    # path('note/<int:note_id>/', views.update_note_view, name='update_note'),
    # path('note/<int:note_id>/delete/', views.delete_note_view, name='delete_note'),
]
