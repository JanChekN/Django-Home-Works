# Generated by Django 4.2.3 on 2023-08-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0008_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='Django/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]