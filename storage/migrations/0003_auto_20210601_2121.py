# Generated by Django 3.1.6 on 2021-06-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20210601_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='cover',
            field=models.ImageField(blank=True, upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='link_path',
            field=models.URLField(max_length=250, unique=True),
        ),
    ]