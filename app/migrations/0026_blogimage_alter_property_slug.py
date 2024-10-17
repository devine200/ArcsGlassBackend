# Generated by Django 5.1.1 on 2024-10-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_blog_description_alter_property_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_post')),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='9e9d5e9c-2b25-4e33-a199-3eab9d0f668f', max_length=255, unique=True),
        ),
    ]
