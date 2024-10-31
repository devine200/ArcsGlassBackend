# Generated by Django 5.1.1 on 2024-10-16 12:32

import django.utils.timezone
import markdownfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_blogcarouselimage_remove_blog_description_bottom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='conver_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=markdownfield.models.MarkdownField(default=django.utils.timezone.now, rendered_field='text_rendered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description_rendered',
            field=markdownfield.models.RenderedMarkdownField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='7066ec8e-94a2-4a3e-a905-94d35169a18c', max_length=255, unique=True),
        ),
    ]