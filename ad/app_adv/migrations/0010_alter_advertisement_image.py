# Generated by Django 4.2.3 on 2023-08-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_adv', '0009_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='Django/media', verbose_name='Изображение'),
        ),
    ]
