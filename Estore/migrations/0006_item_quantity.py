# Generated by Django 2.2.18 on 2022-02-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0005_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
