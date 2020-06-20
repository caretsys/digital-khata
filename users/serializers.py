from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class Customererializer(serializers.HyperlinkedModelSerializer):
    user = serializers.RelatedField(source='User', read_only='True')

    class Meta:
        model = Customer
        fields = ['user', 'phone', 'gender', 'store_name',
                  'country', 'city', 'street', 'landmark']
