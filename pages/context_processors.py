
from .models import *
from articles.models import *

def add_variable_to_context(request):
    last_articles = Article.objects.all()[0:6]
    return {
        'last_articles': last_articles


    }