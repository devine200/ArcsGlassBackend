# Generated by Django 5.1.1 on 2024-10-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_merge_20241015_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_bottom',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_top',
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('COMMERCIAL', 'commercial'), ('RESIDENTIAL', 'residential')], default='duplex', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='6c26bb9a-6c7d-4390-8177-4cd97a330622', max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]