# Generated by Django 5.1.1 on 2024-10-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='8bb81b30-4974-4cd5-94d0-a82eacb6a4cb', max_length=255, unique=True),
        ),
    ]