# Generated by Django 2.2.18 on 2022-02-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
