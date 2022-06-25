import django_filters
from .models import *


class DoctorFilter(django_filters.rest_framework.FilterSet):
    doctor_name = django_filters.CharFilter(name='doctor_name', lookup_expr='contains')
    slug = django_filters.CharFilter(name='slug', lookup_expr='contains')
    direction = django_filters.CharFilter(name='direction')
    description = django_filters.CharFilter(name='description')
    birth_date = django_filters.DateTimeFilter(name='birth_date')
    work_exp = django_filters.NumberFilter(name='work_exp')
    sort_num = django_filters.NumberFilter(name='sort_name')

    class Meta:
        model = Doctor
        fields = ['doctor_name', 'slug', 'direction', 'description', 'birth_date', 'work_exp', 'sort_num', ]
