from django.urls import path
from .views import WaterListView, WaterCreateView, WaterUpdateView

urlpatterns = [
    path('', WaterListView.as_view(), name='water_list'),
    path('create/', WaterCreateView.as_view(), name='water_create'),
    path('update/<int:pk>/', WaterUpdateView.as_view(), name='water_update'),
]

