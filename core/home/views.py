from django.shortcuts import render
from rest_framework import generics 
from .models import Slider_Picture 
from .serializrs import Serializer_Slider_Picture 
from rest_framework import permissions 
from .permissions import Permissions_Edit_Slider 

# Create your views here.


class View_Slider_Picture(generics.ListCreateAPIView):
    queryset = Slider_Picture.objects.all()
    serializer_class = Serializer_Slider_Picture
    
class View_Detail_Slider_Picture(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (Permissions_Edit_Slider,)
    queryset = Slider_Picture.objects.all()
    serializer_class = Serializer_Slider_Picture

    
    
    
    
    
    


