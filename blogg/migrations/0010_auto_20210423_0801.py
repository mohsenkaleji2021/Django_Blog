# Generated by Django 3.2 on 2021-04-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0009_auto_20210423_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
