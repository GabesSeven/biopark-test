from django.urls import path
from .views import index, register, immobile

urlpatterns = [
    path('', index, name='index'),
    path('admin/', index, name='sec-bio'),
    path('register:<int:pg>', register, name='register'),
    path('immobile/<int:pk>', immobile, name='immobile'),
]
