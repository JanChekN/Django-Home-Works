# Generated by Django 4.2.3 on 2023-08-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_adv', '0016_alter_advertisement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(blank=True, help_text='Не обязательно', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, help_text='Не обязательно', null=True, upload_to='media/',
                                    verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Не обязательно', max_digits=100,
                                      null=True, verbose_name='Цена'),
        ),
    ]