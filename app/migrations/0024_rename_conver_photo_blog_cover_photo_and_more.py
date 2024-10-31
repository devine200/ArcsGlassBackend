# Generated by Django 5.1.1 on 2024-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_property_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='conver_photo',
            new_name='cover_photo',
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='8ce22d70-caef-4253-8fa9-a28562691697', max_length=255, unique=True),
        ),
    ]