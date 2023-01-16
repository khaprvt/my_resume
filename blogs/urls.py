from django.urls import path
from .views import BlogModelView


urlpatterns = [
    path('blogs/', BlogModelView.as_view(), name='blogs')
]