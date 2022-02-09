"""
Сигнали дозволяють певним відправникам
сповіщати набір одержувачів про те, що відбулася певна дія.
"""
# !/usr/bin/env python3
# -*- coding=utf-8 -*-

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserRegistrationModel


# Сигнал post_save, запускається після того, як модель
# закінчить виконання методу збереження.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Створює екземпляр користувача для кожного нового користувача
    після реєстрації за допомогою форми UserRegistrationModel.
    """
    if created:
        profile = UserRegistrationModel.objects.create(user=instance)
        profile.save()
