# Generated by Django 4.0.2 on 2022-07-09 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Er',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Er_Brand', models.CharField(max_length=20)),
                ('Er_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Er_Num', models.CharField(blank=True, max_length=20, null=True)),
                ('Er_Add', models.CharField(blank=True, max_length=100, null=True)),
                ('Er_Reservation', models.CharField(blank=True, max_length=500, null=True)),
                ('create_date', models.DateTimeField(null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Th',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Th_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Th_Genre', models.CharField(blank=True, max_length=20, null=True)),
                ('Th_Nop', models.CharField(blank=True, max_length=10, null=True)),
                ('Th_Time', models.CharField(blank=True, max_length=10, null=True)),
                ('Th_Diff', models.CharField(blank=True, max_length=10, null=True)),
                ('Th_Intro', models.TextField(blank=True, max_length=5000, null=True)),
                ('Th_Img1', models.ImageField(blank=True, default='/image/noimage.png', null=True, upload_to='image/th/')),
                ('create_date', models.DateTimeField(null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('er', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keys.er')),
            ],
        ),
    ]
