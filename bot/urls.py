from django.urls.conf import path

from bot.views import TgUserUpdateView

urlpatterns = [
    path("verify", TgUserUpdateView.as_view(), name='verify'),
]