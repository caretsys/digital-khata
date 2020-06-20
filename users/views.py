from django.contrib.auth.models import User
from .models import Customer
from .serializers import Customererializer
from rest_framework import generics


class ListUserView(generics.ListAPIView):

    queryset = Customer.objects.all()
    serializer_class = Customererializer
