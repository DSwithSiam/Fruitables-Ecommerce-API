# Generated by Django 5.0.1 on 2024-01-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_no',
            field=models.CharField(max_length=11),
        ),
    ]
