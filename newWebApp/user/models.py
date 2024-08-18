from django.db import models


class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=50)
    password = models.CharField('Пароль', max_length=250)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
