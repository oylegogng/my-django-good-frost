from django.db import models


# Create your models here.


class Application(models.Model):
    name = models.CharField('Ваше имя', max_length=50)
    phone = models.CharField('Ваш номер телефона', max_length=11, null=False)

    def __str__(self):
        return f'{self.name} - Имя, {self.phone} - номер телефона'
