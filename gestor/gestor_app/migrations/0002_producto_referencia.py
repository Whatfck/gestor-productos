# Generated by Django 5.1.3 on 2024-11-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestor_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="referencia",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
