# Generated by Django 4.2.3 on 2023-08-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0006_rename_advertisement_advertisemen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisemen',
            new_name='Advertisement',
        ),
    ]
