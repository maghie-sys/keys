# Generated by Django 3.2.6 on 2021-08-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('th', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thpic',
            old_name='ThPic_CODE',
            new_name='Th_CODE',
        ),
        migrations.AlterField(
            model_name='thpic',
            name='image',
            field=models.ImageField(blank=True, default='/image/th/', null=True, upload_to='image/th/'),
        ),
    ]