# Generated by Django 2.2.24 on 2025-06-23 17:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(default='', max_length=200, verbose_name='ФИО владельца'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AddField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(default=79986654321, max_length=20, verbose_name='Номер владельца'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
