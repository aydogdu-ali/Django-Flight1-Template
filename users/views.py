from django.shortcuts import render

from django.contrib.auth.models import User

from .serializers import RegisterSerializers

from rest_framework.generics import CreateAPIView

# concrete methodu
class RegisterAPI(CreateAPIView):
    queryset = User.objects.all() #kullanacağımız modeli tanımlıyoruz.
    serializer_class = RegisterSerializers # kullanacağımız serializers tanımlıyoruz.