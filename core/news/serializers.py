from rest_framework import serializers 
from .models import News_Avicenna , Category_News 

class Serializer_Category_News(serializers.ModelSerializer):
    
    class Meta:
        model = Category_News
        fields = "__all__"
        
        
class Serializer_News_Avicenna(serializers.ModelSerializer):
    
    class Meta:
        model = News_Avicenna
        fields = "__all__"
        
        