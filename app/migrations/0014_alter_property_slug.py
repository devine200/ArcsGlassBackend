# Generated by Django 5.1.1 on 2024-10-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='eb40d5a8-3e08-483a-9d03-95cee3d124c9', max_length=255, unique=True),
        ),
    ]