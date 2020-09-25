from django.urls import path
from .views import *
from articles.views import *



urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about', AboutView.as_view(), name = 'about'),
    path('contact', ContactView.as_view(), name = 'contact'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/category/', CategoryView.as_view(), name = 'article_category'),
    path('add_subscriber', subscriber_add, name='subscriber-add'),
    path('<int:pk>/author/', AuthorView.as_view(), name = 'article_author'),
    path('<int:pk>/tag/', TagView.as_view(), name = 'tag'),
]

