# Generated by Django 2.0.7 on 2018-07-13 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_article_population'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Content',
        ),
    ]
