from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=25,verbose_name = "Adı")
    color = models.CharField(max_length=25,verbose_name = "Rengi(İngilizce reng)")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Durum"
        verbose_name_plural = "Durumlar"


class Cities(models.Model):
    name = models.CharField(max_length=25,verbose_name = "Adı")
    slug = models.SmallIntegerField(verbose_name = "Sitede yazılan İl kodu")
    sub_sector_report = models.SmallIntegerField(verbose_name = "son rapor 1")
    sector_report = models.SmallIntegerField(verbose_name = "son rapor 2")
    def __str__(self):
        return f"{self.slug}-{self.name}"
    class Meta:
        verbose_name = "İl"
        verbose_name_plural = "İller"



class Fount(models.Model):
    name = models.CharField(max_length=50,verbose_name = "Adı")
    title = models.CharField(max_length=255,null=True,verbose_name = "Unvan")
    link = models.CharField(max_length=255,null=True,verbose_name = "Site adresi")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Data Kaynağı"
        verbose_name_plural = "Data Kaynakları"


class Companies(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "Kullanıcı")
    city = models.ForeignKey(Cities,on_delete=models.CASCADE,verbose_name = "İl")
    full_name = models.CharField(max_length=255,null=True,verbose_name = "Kişi Adı Soyadı")
    sector = models.CharField(max_length=255,verbose_name = "Sektör")
    name = models.CharField(max_length=255,verbose_name = "Firma unvanı")
    short_name = models.CharField(max_length=11,verbose_name = "Firma unvanı(ilk 11 hanesi)")
    phone = models.CharField(max_length=20,verbose_name = "Telefon numarası")
    site = models.CharField(null=True,max_length=255)
    address = models.CharField(null=True,max_length=255,verbose_name = "Adres")
    personels_caount = models.IntegerField(null=True,verbose_name = "Personel sayısı")
    fount = models.ForeignKey(Fount,on_delete=models.CASCADE,verbose_name = "Data kaynağı")
    status = models.ManyToManyField(Status,blank=True,related_name="status")
    last_status = models.ForeignKey(Status,on_delete=models.CASCADE ,related_name="last_status")
    note = models.TextField(null=True,blank=True,default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    reminder = models.DateTimeField(null=True, default=None)
    def __str__(self):
        return f"{self.city}--{self.name}"
    class Meta:
        unique_together = ('short_name', 'phone',)
        verbose_name = "Data"
        verbose_name_plural = "Datalar"


class AccountReport(models.Model):
    user = models.CharField(max_length=255)
    number = models.IntegerField()
    def __str__(self):
        return f"{self.user}{self.number}"
    class Meta:
        verbose_name = "Hesap raporu"
        verbose_name_plural = "Hesap raporları"



class AgreementStatus(models.Model):
    name = models.CharField(max_length=25,verbose_name = "Adı")
    color = models.CharField(max_length=25,verbose_name = "Rengi(İngilizce reng)")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sözleşme Durumu"
        verbose_name_plural = "Sözleşme Durumları"

class Agreement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "Kullanıcı")
    company_name = models.ForeignKey(Companies,on_delete=models.CASCADE,verbose_name = "Firma unvanı")
    person_name = models.CharField(max_length=255,null=True)
    person_number = models.IntegerField(null=True)
    status = models.ForeignKey(AgreementStatus,on_delete=models.CASCADE,verbose_name = "Sözleşme durumu",null=True)
    record_place = models.CharField(max_length=255,verbose_name = "Çekim yeri",null=True)
    whatsapp = models.IntegerField(null=True)
    mail = models.CharField(max_length=255,null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Sözleşme tarihi")
    record_date = models.DateTimeField(null=True,verbose_name = "Çekim tarihi")
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user}--{self.company_name}"
    class Meta:
        verbose_name = "Sözleşme"
        verbose_name_plural = "Sözleşmeler"
