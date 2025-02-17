from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('threads/', thread_list, name='thread_list'),
    path('threads/<int:thread_id>/', thread_detail, name='thread_detail'),
    path('threads/<int:thread_id>/delete/', delete_thread, name='delete_thread'),
    path('threads/<int:thread_id>/edit/', edit_thread, name='edit_thread'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
]