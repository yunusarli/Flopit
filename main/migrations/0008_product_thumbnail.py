# Generated by Django 4.0 on 2021-12-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_created_product_sold_product_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
