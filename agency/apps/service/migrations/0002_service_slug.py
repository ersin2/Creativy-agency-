# Generated by Django 3.2.9 on 2021-12-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
