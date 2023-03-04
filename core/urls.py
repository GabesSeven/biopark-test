from django.urls import path
from .views import index, register, immobile, sec_bio

urlpatterns = [
    path('immobile/<int:pk>', immobile, name='immobile'),
    path('', index, name='index'),
    path('admin/', sec_bio, name='sec-bio'),
    path('register:<int:pg>', register, name='register'),
]
