from rest_framework import generics, viewsets, filters
from django.shortcuts import render
from .models import Doctor, Direction
from .serializers import DoctorSerializer, DirectionSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .filters import DoctorFilter


class DoctorViewSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorViewSetPagination
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = DoctorFilter
    # search_fields = ('doctor_name', 'slug', 'direction', 'description')
    ordering_fields = ('birth_date', 'work_exp', 'sort_num')
    ordering = ('-work_exp',)


class DirectionAPIView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
