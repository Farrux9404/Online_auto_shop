from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Logo, Car, Contract
from .serializer import LogoSerializers, CarSerializers, ContractSerializers, ContractsubSerializers
from .pagination import ResultsSetPagination


class LogoListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LogoSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Logo.objects.all().order_by('order')


@api_view(['GET'])
def Logodetail(request, pk):
    logo = get_object_or_404(Logo, pk=pk)
    serializer = LogoSerializers(logo, context={'request': request})
    return Response(serializer.data)


class CarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CarSerializers
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Car.objects.all().order_by('order')


@api_view(['GET'])
def Cardetail(request, pk):
    car = get_object_or_404(Logo, pk=pk)
    serializer = CarSerializers(car, context={'request': request})
    return Response(serializer.data)


class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = CarSerializers


@api_view(['GET'])
def Contractdetail(request, pk):
    car = get_object_or_404(Contract, pk=pk)
    serializer = ContractSerializers(car, context={'request': request})
    return Response(serializer.data)