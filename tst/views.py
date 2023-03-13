from django.shortcuts import render
from rest_framework import viewsets
from .models import Tst
from .serializer import TstSerializers

# Create your views here.
class TstView(viewsets.ModelViewSet):
    queryset = Tst.objects.all()
    serializer_class = TstSerializers
