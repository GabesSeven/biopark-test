from django.urls import path
from .views import index, register

urlpatterns = [
    path('', index, name='index'),
    path('admin/', index, name='sec-bio'),
    path('register:<int:pg>', register, name='register'),
]
