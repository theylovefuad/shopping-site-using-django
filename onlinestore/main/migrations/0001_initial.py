# Generated by Django 4.0.4 on 2022-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('price', models.FloatField(default=100.0)),
                ('category', models.CharField(choices=[('Shoes', 'Shoes'), ('Clothing', 'Clothing'), ('Gadgets', 'Gadgets'), ('Home & Appliances', 'Home & Appliances'), ('Others', 'Others')], max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('instructions', models.CharField(choices=[('Available', 'Available'), ('Out of Stock', 'Out of Stock'), ('Shipped from Abroad', 'Shipped from Abroad')], max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
