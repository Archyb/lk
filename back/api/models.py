#create model
from django.db import models
from django.utils.translation import gettext_lazy as _

class Ip(models.Model):
    ip = models.GenericIPAddressField()
    isAuth= models.BooleanField(default=False)
    network=models.ForeignKey('Network',on_delete=models.CASCADE,related_name='ips',null=True,blank=True)

    def __str__(self):
        return self.ip


class Network(models.Model):
    network = models.GenericIPAddressField()
    mask = models.IntegerField()
    isAuth = models.BooleanField(default=False)


    def __str__(self):
        return self.network


class Faq(models.Model):

    class product(models.TextChoices):
        MAIL = 'MAIL', _('Mail')
        JESLASTIC = 'JESLASTIC', _('Jelastic')
        SWISSBACKUP = 'SWISSBACKUP', _('Swissbackup')
        NEWSLETTER = 'NEWSLETTER', _('Newsletter')
        BILLETERIE = 'BILLETERIE', _('Billeterie')
        PUBLICCLOUD = 'PUBLICCLOUD', _('Publiccloud')
        KDRIVE = 'KDRIVE', _('Kdrive')
        KCHAT = 'KCHAT', _('Kchat')
        CALENDRIER = 'CALENDRIER', _('Calendrier')
        VOD_AOD = 'VOD/AOD', _('Vod/Aod')
        SERVERCLOUD = 'SERVERCLOUD', _('Servercloud')
        DOMAINES = 'DOMAINES', _('Domaines')
        SSL = 'SSL', _('Ssl')
        WORKSPACE = 'WORKSPACE', _('Workspace')

    type = models.CharField(max_length=50, choices=product.choices, default=product.MAIL)
    subject = models.CharField(max_length=100)
    url= models.URLField(max_length=200)
    def __str__(self):
        return self.type + ' - ' + self.subject