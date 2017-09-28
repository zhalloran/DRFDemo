from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

image_urls = format_suffix_patterns([
    url(r'^images$', views.ImageListView.as_view()),
    url(r'^images/(?P<image_id>.+)$', views.ImageDetailView.as_view()),
])
