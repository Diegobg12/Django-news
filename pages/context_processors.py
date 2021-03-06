
from .models import *
from articles.models import *
from users.models import *
from taggit.models import Tag

def add_variable_to_context(request):
    categories = Category.objects.all()
    last_articles = Article.objects.all()[0:6]
    tags = Tag.objects.all()
    quote = Quote.objects.last()
    me = CustomUser.objects.first()

    return {
        'last_articles': last_articles,
        'Categories': categories,
        'tags' : tags,
        'quote': quote,
        'me': me,
    }
