from django.urls import path
from .views import CustomLoginView, ChangePasswordView, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='course/home.html'), name='logout'),
    path('profile/', profile, name='users-profile'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
]
