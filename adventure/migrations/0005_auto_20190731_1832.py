# Generated by Django 2.2.3 on 2019-08-01 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0004_auto_20190731_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='e_to',
            new_name='e',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='n_to',
            new_name='n',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='s_to',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='w_to',
            new_name='w',
        ),
    ]
