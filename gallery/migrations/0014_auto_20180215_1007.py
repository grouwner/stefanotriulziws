# Generated by Django 2.0.2 on 2018-02-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_auto_20180214_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photo',
            name='Upload_photo',
            field=models.ImageField(default='', max_length=255, upload_to='../static/'),
        ),
    ]
