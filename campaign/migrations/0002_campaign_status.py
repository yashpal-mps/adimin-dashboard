# Generated by Django 5.1.7 on 2025-03-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("campaign", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("active", "Active"),
                    ("complete", "Complete"),
                    ("cancelled", "Cancelled"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
