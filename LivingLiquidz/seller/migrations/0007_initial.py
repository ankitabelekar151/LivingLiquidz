# Generated by Django 5.0.4 on 2024-04-20 13:37

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0006_remove_product_category_remove_product_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='seller.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('product_image', models.ImageField(blank=True, default='', null=True, upload_to='upload_products')),
                ('price', models.FloatField(blank=True, null=True)),
                ('product_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('quantity', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('size', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('product_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='seller.category')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]