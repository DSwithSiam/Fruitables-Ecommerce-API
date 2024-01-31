# Generated by Django 5.0.1 on 2024-01-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_userprofile_balance_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='patient/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile_no',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]