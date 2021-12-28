from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DetailSerializer
from .models import Detail
# Create your views here.


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all().order_by('name')
    serializer_class = DetailSerializer
