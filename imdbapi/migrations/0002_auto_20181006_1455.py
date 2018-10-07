# Generated by Django 2.1.1 on 2018-10-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='names',
            name='primaryProfession',
            field=models.CharField(default='', help_text='the top-3 professions of the person', max_length=500),
        ),
        migrations.AlterField(
            model_name='titles',
            name='genres',
            field=models.CharField(default='', help_text='Includes up to three genres associated with the title', max_length=500),
        ),
        migrations.AlterField(
            model_name='titles',
            name='isAdult',
            field=models.BooleanField(choices=[(True, '1'), (False, '0')], default=False, help_text='False: non-adult title; True: adult title'),
        ),
    ]