from django.urls import path
from .views import ImageDataCreateView, ImageDataListView, ImageDataDetailView

urlpatterns = [
    path('images/', ImageDataListView.as_view(), name='image-list'),
    path('images/create/', ImageDataCreateView.as_view(), name='image-create'),
    path('images/<int:pk>/', ImageDataDetailView.as_view(), name='image-detail'),
]
