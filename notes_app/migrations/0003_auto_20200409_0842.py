# Generated by Django 3.0.4 on 2020-04-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20200406_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(upload_to=' notes-img'),
        ),
    ]
