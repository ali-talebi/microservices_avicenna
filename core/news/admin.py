from django.contrib import admin
from .models import News_Avicenna , Category_News 
# Register your models here.


@admin.register(Category_News)
class News_Avicenna_Admin(admin.ModelAdmin):
    
    list_display = ["name_category" ,]


@admin.register(News_Avicenna)
class News_Avicenna_Admin(admin.ModelAdmin):
    
    list_display = ["title" , "category"]