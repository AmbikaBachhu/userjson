from django.shortcuts import render
from .models import user, activity,duplicate
from .serializers import userserializer, activityserializer,duplicateserializer
from rest_framework import generics


# Create your views here.


class activityAPI(generics.ListAPIView):
    queryset = duplicate.objects.all()
    serializer_class = duplicateserializer
