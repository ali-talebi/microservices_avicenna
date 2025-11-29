from django.urls import path 
from .views import View_Slider_Picture , View_Detail_Slider_Picture 

app_name = "HOME"
urlpatterns = [
    path('sliders/',View_Slider_Picture.as_view(),name="slider_picture"),
    path('sliders_detail/<int:pk>/',View_Detail_Slider_Picture.as_view(),name="detail_slider"),
    
    
]
