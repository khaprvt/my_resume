from django.urls import path
from .views import WorkListView, WorkDetailView

urlpatterns = [
    path('works/', WorkListView.as_view(), name='works'),
    path('work/detail/<int:pk>/', WorkDetailView.as_view(), name='work-detail')
]