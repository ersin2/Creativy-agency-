# Generated by Django 3.2.9 on 2021-12-13 14:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_socialmedia_icon_socmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='о себе'),
        ),
    ]
