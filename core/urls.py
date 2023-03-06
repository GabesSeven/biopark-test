from django.urls import path
from .views import index, register, immobile, sec_bio

urlpatterns = [
    path('', index, name='index'),
    path('admin/', sec_bio, name='sec-bio'),
    path('register:<int:pg>', register, name='register'),
    path('immobile/<int:pk>/<int:pg>', immobile, name='immobile'),
]
