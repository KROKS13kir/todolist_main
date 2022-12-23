import string
from random import sample

from django.db import models
from core.models import User


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField(verbose_name='TG CHAT_ID')
    tg_user_id = models.BigIntegerField(unique=True, verbose_name='TG USER_ID')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, default=None)
    verification_code = models.CharField(max_length=10, unique=True)
    username = models.CharField(
        max_length=255,
        verbose_name='TG USERNAME',
        null=True,
        blank=True,
        default=None
    )

    def set_verification_code(self) -> None:
        length = 10  # Длина кода подтверждения
        digits = string.digits
        verif_code = ''.join(sample(digits, length))
        self.verification_code = verif_code

    class Meta:
        verbose_name = 'TG User'
        verbose_name_plural = 'TG Users'