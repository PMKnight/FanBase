from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('memories/', views.MemoryList.as_view(), name='memory-list'),
    path('memories/<int:pk>', views.MemoryDetail.as_view(), name='memory_detail'),

]
