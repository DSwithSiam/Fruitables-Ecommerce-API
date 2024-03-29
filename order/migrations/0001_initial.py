# Generated by Django 5.0.1 on 2024-01-28 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_add_to_card'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('payment', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product.product')),
            ],
        ),
    ]
