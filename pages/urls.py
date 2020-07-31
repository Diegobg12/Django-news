from django.urls import path
from .views import *
from articles.views import *


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about', AboutView.as_view(), name = 'about'),
    path('contact', ContactView.as_view(), name = 'contact'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/category/', CategoryView.as_view(), name = 'article_category'),

]