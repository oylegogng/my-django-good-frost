# Generated by Django 3.2.12 on 2022-03-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('phone', models.CharField(max_length=11, verbose_name='(8(999) 999 99 99 )')),
            ],
        ),
    ]