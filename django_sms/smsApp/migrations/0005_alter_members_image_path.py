# Generated by Django 4.1.7 on 2023-05-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smsApp", "0004_alter_members_image_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="image_path",
            field=models.ImageField(blank=True, default=0, null=True, upload_to=""),
        ),
    ]
