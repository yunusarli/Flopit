# Generated by Django 4.0 on 2021-12-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_product_tags_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='main.Tag'),
        ),
    ]
