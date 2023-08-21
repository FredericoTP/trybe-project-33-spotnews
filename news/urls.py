from django.urls import path
from news.views import home, news_details, create_category


urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", create_category, name="categories-form"),
]
