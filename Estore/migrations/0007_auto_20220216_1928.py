# Generated by Django 2.2.18 on 2022-02-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0006_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
