# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.contrib.auth.models import User

from .pagination import PaginationPageNumber

from misiones.models import Mision, Medicion

# Create your views here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','get_full_name', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

#Medicion serializers
class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = "__all__"

#Medicion min serializers
class MedicionMinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medicion
        fields = ('mision','data','fecha_creacion','fecha_eliminacion')


#Mision serializers
class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = "__all__"

#Mision min serializers
class MisionMinSerializer(serializers.ModelSerializer):
    mediciones = MedicionMinSerializer(many=True, read_only=True)
    comandante = UserSerializer(read_only=True)
    comandanteId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='usuario')
    
    class Meta:
        model = Mision
        fields = ('id','nombre','comandante','comandanteId','latitud','longitud','descripcion','estado','fecha_creacion','fecha_fin','mediciones')


#Mision list create view
class MisionList(generics.ListCreateAPIView):
    queryset = Mision.objects.filter(fecha_eliminacion=None)
    serializer_class = MisionSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)
    pagination_class = PaginationPageNumber

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data['comandante'] = user.id
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'message': 'Registro guardado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200, headers=headers)

#Mision  detail view 
class MisionDetail(generics.RetrieveUpdateAPIView):
    queryset = Mision.objects.all()
    serializer_class = MisionSerializer
    http_method_names = ['put','get','patch']
    permission_classes = (AllowAny,)

    def patch(self, request, pk):
        instance = self.queryset.get(pk=pk)
        request.data['fecha_actualizacion'] = timezone.now()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        serializer.save()
        data = {'message': 'Registro actualizado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200)

# Mision minview api for Client
class MisionMinList(generics.ListAPIView):
    queryset = Mision.objects.filter(fecha_eliminacion=None)
    serializer_class = MisionMinSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    @list_route(methods=['GET'])
    def list(self, request, *args, **kwargs):
        query = Mision.objects.filter(fecha_eliminacion=None)
        queryset = self.filter_queryset(query)
        serializer = self.get_serializer(queryset, many=True)

        if serializer:
            data = {'message': 'lista de Misiones', 'code': 1, 'data': serializer.data}
            return Response(data, status=200)
        else:
            data = {'message': 'lista de Misiones', 'code': 1, 'data': []}
            return Response(data, status=200)

#Medicion list create view
class MedicionList(generics.ListCreateAPIView):
    queryset = Medicion.objects.filter(fecha_eliminacion=None)
    serializer_class = MedicionSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)
    pagination_class = PaginationPageNumber

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'message': 'Registro guardado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200, headers=headers)

#Medicion  detail view 
class MedicionDetail(generics.UpdateAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
    http_method_names = ['put']
    permission_classes = (AllowAny,)

    def put(self, request, pk):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        serializer.save()
        data = {'message': 'Registro actualizado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200)

# Medicion minview api for Client
class MedicionMinList(generics.ListAPIView):
    queryset = Medicion.objects.filter(fecha_eliminacion=None)
    serializer_class = MedicionMinSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    @list_route(methods=['GET'])
    def list(self, request, *args, **kwargs):
        query = Medicion.objects.filter(fecha_eliminacion=None)
        queryset = self.filter_queryset(query)
        serializer = self.get_serializer(queryset, many=True)

        if serializer:
            data = {'message': 'lista de Mediciones', 'code': 1, 'data': serializer.data}
            return Response(data, status=200)
        else:
            data = {'message': 'lista de Mediciones', 'code': 1, 'data': []}
            return Response(data, status=200)


# Mision minview api for Client
class LastMisionMinList(generics.ListAPIView):
    queryset = Mision.objects.filter(fecha_eliminacion=None).last()
    serializer_class = MisionMinSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    @list_route(methods=['GET'])
    def list(self, request, *args, **kwargs):
        # query = Mision.objects.filter(fecha_eliminacion=None)
        query = Mision.objects.filter(fecha_eliminacion=None).last()

        queryset = self.filter_queryset(query)
        serializer = self.get_serializer(queryset, many=False)

        if serializer:
            data = {'message': 'ultima mision', 'code': 1, 'data': serializer.data}
            return Response(data, status=200)
        else:
            data = {'message': 'ultima mision', 'code': 1, 'data': []}
            return Response(data, status=200)