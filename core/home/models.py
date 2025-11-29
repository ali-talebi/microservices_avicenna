from django.db import models
from django.contrib.auth.models import User 
# Create your models here.



class Slider_Picture(models.Model):
    user_created = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sliders' , null = True ) 
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="slider/")
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title or "Slider Item"
    
    class Meta:
        db_table = "slider_picture"
        verbose_name_plural = "slider_picture"
        
    