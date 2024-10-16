# Generated by Django 4.2.16 on 2024-10-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_project_created_at_alter_projectimage_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="blogimage",
            name="image",
            field=models.ImageField(upload_to="blog"),
        ),
        migrations.AlterField(
            model_name="landingpagecarousel",
            name="cover_photo",
            field=models.ImageField(upload_to="landing"),
        ),
        migrations.AlterField(
            model_name="landingpageprojectsintro",
            name="cover_photo",
            field=models.ImageField(upload_to="landing"),
        ),
    ]
