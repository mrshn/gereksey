# Generated by Django 2.1 on 2019-09-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20190920_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Aktiflik',
            field=models.CharField(default='AKTİF', max_length=100),
        ),
    ]