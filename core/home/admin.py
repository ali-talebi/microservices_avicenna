from django.contrib import admin
from .models import Slider_Picture  
# Register your models here.



@admin.register(Slider_Picture)
class Slider_Picture_Admin(admin.ModelAdmin):
    
    list_display = ['title','link','order']
    
    
    # def show_picture(self,obj):
    #     pass 
    
    # show_picture.short_description = "picture"