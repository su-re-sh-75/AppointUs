from rest_framework import serializers
from django.contrib.auth.models import User

#Python Format to JSON Format
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']