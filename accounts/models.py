from django.db import models
from django.conf import settings


class UserRegistrationModel(models.Model):
    """
    Містить OneToOneField() з інформацією,
    що стосується конкретного користувача.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name='Користувач')
