# Generated by Django 5.0 on 2024-01-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page5", "0007_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="pro_catid",
            field=models.IntegerField(null=True),
        ),
    ]