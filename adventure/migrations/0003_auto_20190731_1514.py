# Generated by Django 2.2.3 on 2019-07-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20190731_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='e_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='n_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='s_to',
        ),
        migrations.RemoveField(
            model_name='room',
            name='w_to',
        ),
        migrations.AddField(
            model_name='room',
            name='e',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='room',
            name='n',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='room',
            name='s',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='room',
            name='w',
            field=models.IntegerField(default=-1),
        ),
    ]
