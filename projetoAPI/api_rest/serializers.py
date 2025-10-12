from rest_framework import serializers

from .models import User

class modelSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = '__all__'