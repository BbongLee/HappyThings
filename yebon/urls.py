from django.urls import path
from . import views

urlpatterns = [
    path('', views.thing_list, name='thing_list'), #thing_list라는 view가 루트 URL에 할당 됨
    
]