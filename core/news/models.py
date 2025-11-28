from django.db import models

# Create your models here.



class Category_News(models.Model):
    
    name_category = models.CharField(max_length=100)
    translate_category = models.CharField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.name_category}'
    
    
    class Meta:
        db_table = "Category_News"
        verbose_name_plural = "category_news"
        



class News_Avicenna(models.Model):
    
    title = models.CharField(max_length=100)
    translate_title = models.CharField(max_length=100,null=True,blank=True)
    picture_1 = models.FileField(null=True,blank=True)
    picture_2 = models.FileField(null=True,blank=True)
    picture_3 = models.FileField(null=True,blank=True)
    picture_4 = models.FileField(null=True,blank=True)
    
    
    category = models.ForeignKey(Category_News,related_name="news",on_delete=models.CASCADE)
    
    
    body = models.TextField(null=True,blank=True)
    translate_body = models.TextField(null=True,blank=True)
    
    
    time_created = models.DateTimeField(auto_now_add=True)
    time_update  = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return f'{self.title}'
    
    
    
    class Meta:
        db_table = "News_Avicenna"
        verbose_name_plural = "news_avicenna"
    
    
    
    
    
    
    