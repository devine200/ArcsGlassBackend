# Generated by Django 5.1.1 on 2024-10-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_blogimage_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='c62800b2-02de-4342-98c6-b07cc5a3d0e6', max_length=255, unique=True),
        ),
    ]
