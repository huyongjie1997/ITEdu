# Generated by Django 2.0.3 on 2019-10-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20191007_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoinfo',
            name='video_source',
            field=models.FileField(default='', max_length=200, upload_to='video/', verbose_name='视频资源'),
        ),
    ]
