# Generated by Django 5.1.1 on 2024-10-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='fd5bc728-6a95-43f2-b7a4-cfd90194a916', max_length=255, unique=True),
        ),
    ]
