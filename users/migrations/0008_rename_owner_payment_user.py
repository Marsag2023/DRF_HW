# Generated by Django 4.2.2 on 2024-07-08 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_payment_link_payment_session_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="owner",
            new_name="user",
        ),
    ]
