# Generated by Django 5.0 on 2023-12-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page5", "0002_rename_reg_mobile_registration_reg_mob_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="reg_mob",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="registration",
            name="reg_pwd",
            field=models.CharField(max_length=255),
        ),
    ]
