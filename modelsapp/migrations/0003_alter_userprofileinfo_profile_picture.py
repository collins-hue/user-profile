# Generated by Django 4.1.4 on 2023-10-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0002_alter_userprofileinfo_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.FileField(default='avi.jpg', upload_to='static/profile_pic1697447428.6277218'),
        ),
    ]
