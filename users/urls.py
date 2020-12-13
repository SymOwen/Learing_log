"""Define URL patterns for users"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', LogoutView.as_view(), name='logout'),
    # Registration page
    path('register/', views.register, name='register')
]
