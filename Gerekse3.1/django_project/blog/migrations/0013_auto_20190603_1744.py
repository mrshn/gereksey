# Generated by Django 2.1 on 2019-06-03 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190603_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ilan_resmi',
            new_name='image',
        ),
    ]