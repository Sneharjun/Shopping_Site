# Generated by Django 5.0 on 2024-01-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page5", "0006_alter_product_pro_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("cat_name", models.CharField(max_length=255)),
                ("cat_image", models.FileField(upload_to="categories")),
            ],
        ),
    ]
