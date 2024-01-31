# Generated by Django 5.0.1 on 2024-01-26 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='product.category'),
        ),
        migrations.CreateModel(
            name='Rateing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rateing', models.CharField(choices=[('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rateing', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='product.product')),
            ],
        ),
    ]