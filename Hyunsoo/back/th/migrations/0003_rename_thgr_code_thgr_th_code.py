# Generated by Django 3.2.6 on 2021-10-10 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('th', '0002_rename_th_code_thgr_thgr_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thgr',
            old_name='ThGr_CODE',
            new_name='Th_CODE',
        ),
    ]