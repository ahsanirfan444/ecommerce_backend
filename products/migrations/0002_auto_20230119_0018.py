# Generated by Django 3.1 on 2023-01-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='new_arrivals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='offer_badge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='popular_items',
            field=models.BooleanField(default=False),
        ),
    ]