# create serializer
from rest_framework import serializers
from api.models import Ip, Network, Faq


class IpSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = Ip
        fields = '__all__'
        #show netowrk in ip
        depth = 1



class NetworkSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = Network
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = Faq
        fields = '__all__'