# Generated by Django 4.1.4 on 2023-03-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurgu', '0006_alter_kj_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kj',
            name='play_time_as_minuate',
            field=models.CharField(blank=True, default='', max_length=60, verbose_name='Yayın dakikasi'),
        ),
    ]