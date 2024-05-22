# Generated by Django 3.2.25 on 2024-05-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0005_auto_20240506_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.TextField(default='P.O BOX 140', max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='city',
            field=models.TextField(default='Nairobi', max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.FileField(default='20240311_081940.jpg', upload_to='static/profile_pic1714987081.5886946'),
        ),
    ]
