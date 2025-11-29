from rest_framework import serializers 
from .models import Slider_Picture 



class Serializer_Slider_Picture(serializers.ModelSerializer):
    
    class Meta:
        model  = Slider_Picture
        fields = "__all__"
         


