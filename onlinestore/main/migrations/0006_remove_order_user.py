# Generated by Django 4.0.4 on 2022-06-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order_sesh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
