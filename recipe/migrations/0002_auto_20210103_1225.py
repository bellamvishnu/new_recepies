# Generated by Django 3.1 on 2021-01-03 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredians',
            new_name='ingre',
        ),
    ]
