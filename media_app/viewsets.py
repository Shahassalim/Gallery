from rest_framework import viewsets
from . import models
from . import serializers

class ImgViewset(viewsets.ModelViewSet):
    queryset=models.ImgModel.objects.all()
    serializer_class=serializers.ImgModelSerializer