from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addstudent/', views.addrecord, name='addstudent'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/<str:id>', views.update, name='update'),
    path('update/updaterecord/<str:id>', views.updaterecord, name='updaterecord'),
]

