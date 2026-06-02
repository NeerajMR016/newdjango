from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name="index"),
    path('prod', product, name="product"),
    path('addproduct', addproduct, name="add"),
]