from django.urls import path 
from .views import View_Category_News, View_News_Avicenna , View_Category_News_Detail , View_News_Avicenna_Detail


app_name = "news_avicenna"

urlpatterns = [
    path("category_news/",View_Category_News.as_view(),name="total_category_news"),
    path("detail_category_news/<int:pk>/",View_Category_News_Detail.as_view(),name="detail_category_news"),
    path("news/",View_News_Avicenna.as_view(),name="total_news_avicenna"),
    path("detail_news/<int:pk>/",View_News_Avicenna_Detail.as_view(),name="detail_news_avicenna"),
]
