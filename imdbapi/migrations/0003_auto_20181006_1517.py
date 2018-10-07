# Generated by Django 2.1.1 on 2018-10-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbapi', '0002_auto_20181006_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='isAdult',
            field=models.CharField(choices=[(True, '1'), (False, '0')], default=False, help_text='False: non-adult title; True: adult title', max_length=2),
        ),
    ]