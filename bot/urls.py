from django.urls.conf import path

from bot.views import VerificationView

urlpatterns = [
    path("verify", VerificationView.as_view(), name='verify'),
]