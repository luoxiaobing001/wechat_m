# Generated by Django 2.0.7 on 2018-07-13 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='population',
        ),
    ]
