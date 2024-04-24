# Generated by Django 5.0.4 on 2024-04-19 09:30

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0004_remove_products_categories_remove_products_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('product_image', models.ImageField(blank=True, upload_to='upload_products')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='seller.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('product_image', models.ImageField(blank=True, upload_to='upload_products')),
                ('selling_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]