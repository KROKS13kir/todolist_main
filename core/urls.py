from django.urls.conf import path
from core import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('profile', views.UserRetrieveUpdateView.as_view(), name='profile'),
    path('login', views.LoginView.as_view(), name='login'),
    path('update_password', views.PasswordUpdateView.as_view(), name='update_password'),
]
