from django.urls import path
from exemple_app import views

urlpatterns = [
    path('',views.index_exemple_app, name='index'),
    path('add/',views.new_entry,name='new_entry'),
]
