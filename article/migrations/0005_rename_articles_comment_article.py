# Generated by Django 3.2.6 on 2021-09-05 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_rename_article_comment_articles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='articles',
            new_name='article',
        ),
    ]
