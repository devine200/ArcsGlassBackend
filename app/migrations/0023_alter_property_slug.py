# Generated by Django 5.1.1 on 2024-10-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_blog_client_remove_blog_collaborator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='53bd992a-720b-4b49-9fd5-8065d756fd8f', max_length=255, unique=True),
        ),
    ]
