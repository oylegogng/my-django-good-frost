# Generated by Django 3.2.12 on 2022-03-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Ваш номер телефона'),
        ),
    ]