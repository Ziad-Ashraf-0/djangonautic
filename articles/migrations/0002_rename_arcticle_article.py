# Generated by Django 4.2.9 on 2024-02-01 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Arcticle", new_name="Article",),
    ]
