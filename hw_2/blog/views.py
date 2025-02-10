from django.http import JsonResponse
from .models import Article

def get_articles(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def get_article_by_id(request, article_id):
    article = Article.objects.filter(id=article_id).values().first()
    return JsonResponse(article, safe=False) if article else JsonResponse({'error': 'Article not found'}, status=404)

# Create your views here.
