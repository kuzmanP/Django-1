# Generated by Django 2.2.18 on 2022-02-20 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0011_auto_20220220_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]