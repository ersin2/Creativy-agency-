# Generated by Django 3.2.9 on 2021-12-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_team_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
