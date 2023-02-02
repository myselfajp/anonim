# Generated by Django 4.1.4 on 2023-01-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0025_accountreport_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='Contract_minute',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='price',
            field=models.CharField(default='2250', max_length=255, verbose_name='Sözleşme bedeli'),
        ),
    ]