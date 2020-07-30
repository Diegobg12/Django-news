from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('<int:pk>/edituser/', EditUser.as_view(), name = 'edituser')
]