from django.urls import path
from .views import get_articles, get_article_by_id

urlpatterns = [
    path('articles/', get_articles, name='get_articles'),
    path('articles/<int:article_id>/', get_article_by_id, name='get_article_by_id'),
]