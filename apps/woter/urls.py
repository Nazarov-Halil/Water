from django.urls import path
from .views import WaterListView, WaterCreateView, WaterUpdateView,WaterDeleteView

urlpatterns = [
    path('', WaterListView.as_view(), name='water_list'),
    path('create/', WaterCreateView.as_view(), name='water_create'),
    path('update/<int:pk>/', WaterUpdateView.as_view(), name='water_update'),
    path('delete/<int:pk>', WaterDeleteView.as_view(), name='water_delete')
]

