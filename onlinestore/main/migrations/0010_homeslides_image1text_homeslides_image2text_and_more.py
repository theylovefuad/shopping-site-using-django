# Generated by Django 4.0.4 on 2022-06-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_homeslides_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslides',
            name='image1text',
            field=models.CharField(default='change', max_length=10000),
        ),
        migrations.AddField(
            model_name='homeslides',
            name='image2text',
            field=models.CharField(default='change', max_length=10000),
        ),
        migrations.AddField(
            model_name='homeslides',
            name='image3text',
            field=models.CharField(default='change', max_length=10000),
        ),
    ]