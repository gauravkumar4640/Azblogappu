# Generated by Django 4.0.5 on 2022-07-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
