# Generated by Django 4.1.4 on 2023-03-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0033_azexport_is_verified'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companies',
            unique_together=set(),
        ),
    ]
