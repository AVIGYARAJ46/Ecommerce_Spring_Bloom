# Generated by Django 3.2.23 on 2024-01-29 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowerbloom', '0005_auto_20240129_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='delivery_duration',
            new_name='delivery_info',
        ),
    ]
