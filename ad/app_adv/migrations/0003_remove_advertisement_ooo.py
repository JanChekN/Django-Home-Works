# Generated by Django 4.2.3 on 2023-07-29 00:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app_adv', '0002_rename_advert_advertisement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='ooo',
        ),
    ]
