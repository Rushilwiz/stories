# Generated by Django 5.0.7 on 2024-08-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AddField(
            model_name="user",
            name="full_name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Full Name"
            ),
        ),
    ]
