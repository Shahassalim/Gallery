from pyexpat import model
from rest_framework import serializers
from .models import ImgModel

class ImgModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImgModel
        fields='__all__'