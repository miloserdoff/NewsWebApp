# Generated by Django 5.0.7 on 2024-08-14 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]