from django.urls import path, include
from barcode_app import views

urlpatterns = [
    path('', views.index, name='index'),            #default index page url 
]

