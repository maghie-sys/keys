# Generated by Django 3.2.6 on 2021-11-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('th', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fc_Name', models.CharField(max_length=20)),
                ('Fc_Num', models.CharField(max_length=20, null=True)),
                ('Fc_Brn', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
