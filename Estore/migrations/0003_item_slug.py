# Generated by Django 2.2.18 on 2022-02-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0002_auto_20220215_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
