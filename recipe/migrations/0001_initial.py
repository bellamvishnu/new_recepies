# Generated by Django 2.2.6 on 2020-02-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredians', models.CharField(max_length=100)),
                ('process', models.CharField(max_length=100)),
            ],
        ),
    ]
