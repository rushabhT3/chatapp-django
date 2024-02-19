from django.urls import path
from . import views
# from .views import create_note_view

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('notes/create/', views.create_note_view, name='create_note'),
    path('notes/<int:id>/', views.get_note, name='get_note'),
    # path('note/<int:note_id>/', views.update_note_view, name='update_note'),
    # path('note/<int:note_id>/delete/', views.delete_note_view, name='delete_note'),
]
