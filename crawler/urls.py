from django.urls import path
from .views import http_crawler_tobb,http_crawler_google

app_name="crawler"

urlpatterns = [
    path("crawler-<int:city_slug>",http_crawler_tobb,name='tobb'),
    path("crawler_google",http_crawler_google,name='google_map_crawler'),


]
