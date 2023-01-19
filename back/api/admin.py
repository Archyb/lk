from django.contrib import admin

from api.models import Ip, Network, Faq

# Register your models here.
admin.site.register(Ip)
admin.site.register(Network)
admin.site.register(Faq)