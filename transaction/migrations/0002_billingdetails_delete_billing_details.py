# Generated by Django 5.0.1 on 2024-01-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('town_or_city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('order_note', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Billing_details',
        ),
    ]
