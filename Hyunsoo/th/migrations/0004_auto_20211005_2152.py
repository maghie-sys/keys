# Generated by Django 3.2.6 on 2021-10-05 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('th', '0003_rename_image_thpic_th_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='th',
            name='Th_Review',
        ),
        migrations.AlterField(
            model_name='thpic',
            name='Th_pic',
            field=models.ImageField(blank=True, default='/image/noimage.png', null=True, upload_to='image/th/'),
        ),
        migrations.CreateModel(
            name='all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ThPic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='th.thpic')),
                ('er', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='th.er')),
                ('erad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='th.erad')),
                ('th', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='th.th')),
                ('thgr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='th.thgr')),
            ],
        ),
    ]
