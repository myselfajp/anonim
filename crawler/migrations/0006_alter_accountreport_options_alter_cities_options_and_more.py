# Generated by Django 4.1.4 on 2023-01-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crawler', '0005_companies_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountreport',
            options={'verbose_name': 'Hesap raporu', 'verbose_name_plural': 'Hesap raporları'},
        ),
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'İl', 'verbose_name_plural': 'İller'},
        ),
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name': 'Data', 'verbose_name_plural': 'Datalar'},
        ),
        migrations.AlterModelOptions(
            name='fount',
            options={'verbose_name': 'Data Kaynağı', 'verbose_name_plural': 'Data Kaynakları'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Durum', 'verbose_name_plural': 'Durumlar'},
        ),
        migrations.AddField(
            model_name='companies',
            name='reminder',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='sector_report',
            field=models.SmallIntegerField(verbose_name='son rapor 2'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='slug',
            field=models.SmallIntegerField(verbose_name='Sitede yazılan İl kodu'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='sub_sector_report',
            field=models.SmallIntegerField(verbose_name='son rapor 1'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.cities', verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='fount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.fount', verbose_name='Data kaynağı'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Kişi Adı Soyadı'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Firma unvanı'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='personels_caount',
            field=models.IntegerField(verbose_name='Personel sayısı'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefon numarası'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='sector',
            field=models.CharField(max_length=255, verbose_name='Sektör'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='short_name',
            field=models.CharField(max_length=11, verbose_name='Firma unvanı(ilk 11 hanesi)'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='fount',
            name='link',
            field=models.CharField(max_length=255, verbose_name='Site adresi'),
        ),
        migrations.AlterField(
            model_name='fount',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='fount',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Unvan'),
        ),
        migrations.AlterField(
            model_name='status',
            name='color',
            field=models.CharField(max_length=25, verbose_name='Rengi(İngilizce reng)'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Adı'),
        ),
    ]
