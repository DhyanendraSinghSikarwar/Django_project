from django.urls import path
from . import views

urlpatterns = [
	  path('',views.root,name = 'root'),
      path('members/',views.members,name = 'members'),
      path('testing/',views.testing,name = 'testing'),
      path('myapp/',views.myapp,name = 'myapp'),
      path('members/details/<int:id>',views.details,name = 'details')
      ]