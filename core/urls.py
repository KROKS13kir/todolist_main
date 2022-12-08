from django.urls.conf import path

from core.views import SignUpView, LoginView, UserRetrieveUpdateView, PasswordUpdateView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserRetrieveUpdateView.as_view()),
    path('update_password', PasswordUpdateView.as_view())
]
