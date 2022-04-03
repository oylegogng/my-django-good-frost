from django.db import models

# Create your models here.

class feedback(models.Model):
    author_name = models.CharField('Ваше имя', max_length=50)
    feedback_text = models.CharField('Текст отзыва', max_length= 250)

    def __str__(self):
        return f'{self.author_name}: {self.feedback_text}'

