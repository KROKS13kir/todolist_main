from django.urls.conf import path

import core.views as views

urlpatterns = [
    path('signup', views.SignUpView.as_view()),
    path('login', views.LoginView.as_view()),
    path('profile', views.UserRetrieveUpdateView.as_view()),
    path('update_password', views.PasswordUpdateView.as_view())
]
