# Generated by Django 2.1 on 2019-06-09 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190608_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='relevance',
            field=models.IntegerField(choices=[('', 'Hepsi'), (1, 'Satılık'), (2, 'Kiralık')], default=1, validators=[django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[('', 'Hepsi'), (1, 'Eğlence'), (2, 'Kitap'), (3, 'Ulaşım'), (4, 'Hizmet')], default=1, validators=[django.core.validators.MaxValueValidator(500)]),
        ),
    ]