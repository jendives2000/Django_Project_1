# Generated by Django 5.0.3 on 2024-03-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_add_slug_to_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip",
            field=models.IntegerField(default="0000"),
            preserve_default=False,
        ),
    ]
