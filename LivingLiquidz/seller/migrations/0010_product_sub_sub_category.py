# Generated by Django 5.0.4 on 2024-05-24 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_remove_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.sub_sub_category'),
            preserve_default=False,
        ),
    ]
