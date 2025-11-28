from django.shortcuts import render
from .serializers import Serializer_Category_News , Serializer_News_Avicenna 
from .models import News_Avicenna , Category_News 
from rest_framework import generics 
# Create your views here.



class View_Category_News(generics.ListCreateAPIView):
    
    queryset = Category_News.objects.all()
    serializer_class = Serializer_Category_News

class View_Category_News_Detail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Category_News.objects.all()
    serializer_class = Serializer_Category_News



class View_News_Avicenna(generics.ListCreateAPIView):
    
    queryset = News_Avicenna.objects.all()
    serializer_class = Serializer_News_Avicenna

class View_News_Avicenna_Detail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = News_Avicenna.objects.all()
    serializer_class = Serializer_News_Avicenna