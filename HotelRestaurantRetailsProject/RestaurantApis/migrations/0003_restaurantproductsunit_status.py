# Generated by Django 4.2.6 on 2023-11-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApis', '0002_restaurantorder_categoryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantproductsunit',
            name='Status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Passive', 'Passive')], default='Active', max_length=200, null=True, verbose_name='Status'),
        ),
    ]