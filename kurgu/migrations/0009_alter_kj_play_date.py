# Generated by Django 4.1.4 on 2023-01-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurgu', '0008_alter_kj_play_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kj',
            name='play_date',
            field=models.CharField(default='', max_length=250, verbose_name='Yayın tarihi'),
        ),
    ]
