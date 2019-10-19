# Generated by Django 2.1 on 2019-06-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190603_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='relevance',
            field=models.IntegerField(choices=[(1, 'Satılık'), (2, 'Kiralık')], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'Hepsi'), (2, 'Eğlence'), (3, 'Kitap'), (4, 'Ulaşım'), (5, 'Hizmet')], default=1),
        ),
    ]
