from rest_framework import serializers
from .models import Logo, Car, Contract, Contractsub


class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['title', 'descriptions', 'image', 'order', 'create', 'update',]


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['title', 'descriptions', 'filed_km', 'year', 'order', 'price', 'logo', 'color', 'image', 'create',
                  'update']


class ContractSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['car', 'create', 'update',]


class ContractsubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contractsub
        fields = ['inital_payment', 'month', 'year', 'contract',]
