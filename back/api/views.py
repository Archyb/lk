import json

from django.http import HttpResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet

from api.dnslookup import creatDnsZone, whoisDomain, ping
from api.models import Ip, Network, Faq
from api.serializers import IpSerializer, NetworkSerializer, FaqSerializer
from django.views.generic import TemplateView

# creat a view  fom a function creatDnsZone
class zoneView(View):
    def get(self, request):
        domain = request.GET.get('domain')
        if domain:
            zone = creatDnsZone(domain)
            return HttpResponse(json.dumps(zone), content_type='application/json')
        else:
            print(request.GET)
            return HttpResponse("Please Enter a Domain")


class whoisView(View):
    def get(self, request):
        domain = request.GET.get('domain')
        if domain:
            print(domain)
            whois = whoisDomain(domain)
            return HttpResponse(json.dumps(whois, indent=4, sort_keys=True, default=str))
        else:
            return HttpResponse("Please Enter a Domain")


class ipView(ModelViewSet):
    queryset = Ip.objects.all()
    serializer_class = IpSerializer

    # get request find by ip
    def get_queryset(self):
        ip = self.request.GET.get('ip')
        if ip is not None:
            return Ip.objects.filter(ip=ip)
        else:
            return HttpResponse("This is not a Infomaniak Ip")


class NetworkView(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class FaqView(ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def get_queryset(self):
        queryset = Faq.objects.all()
        category = self.request.GET.get('category', None)
        print(category)
        if category is not None:
            queryset = queryset.filter(type=category.upper())
        return queryset


class PingView(View):
    def get(self, request):
        ip = request.GET.get('ip')
        if ip is not None:
            print(ip)
            whois = ping(ip)
            return HttpResponse(json.dumps(whois, indent=4, sort_keys=True, default=str))
        else:
            return HttpResponse(json.dumps("info not found", indent=4, sort_keys=True, default=str))

