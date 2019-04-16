from django.db import models
from django import forms


class TodoList(models.Model):
    task = models.CharField(max_length=100)

    TO_DO = 'Надо сделать'
    DONE = 'Сделано'
    CANCELED = 'Отменено'

    STATUSES = (
        (TO_DO, 'Надо сделать'),
        (DONE, 'Сделано'),
        (CANCELED, 'Отменено'),
    )

    status = models.CharField(max_length=15, choices=STATUSES, default=TO_DO)

    def __str__(self):
        return self.task


