# Generated by Django 3.2.25 on 2024-05-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0006_auto_20240506_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.FileField(default='20240311_081940.jpg', upload_to='static/profile_pic1715003060.4684038'),
        ),
    ]