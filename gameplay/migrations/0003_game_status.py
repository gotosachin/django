# Generated by Django 2.1.7 on 2019-04-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_auto_20190407_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default='F', max_length=1),
        ),
    ]
