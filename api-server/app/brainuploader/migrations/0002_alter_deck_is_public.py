# Generated by Django 4.2.16 on 2024-12-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainuploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Public?'),
        ),
    ]
