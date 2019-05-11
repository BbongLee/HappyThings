from django.urls import path
from . import views

urlpatterns = [
 	#thing_list라는 view가 루트 URL에 할당 됨
    path('', views.thing_list, name='thing_list'),
    #URL이 thing문자를 포함해야한다는 것을 말함.
    path('thing/<int:pk>/', views.thing_detail, name='thing_detail'),
    path('thing/new', views.thing_new, name='thing_new'),
	path('thing/<int:pk>/edit/', views.thing_edit, name='thing_edit'),
]