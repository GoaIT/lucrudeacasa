from django.urls import path
from forms_app import views

urlpatterns = [
    path('',views.index_forms_app, name='index'),
    path('basic/',views.form_name_view_post,name='post'),
    path('check/',views.form_name_view_check,name='check'),
    path('validate/',views.form_name_view_validation,name='validators'),
    path('usersimpleform/',views.users_views, name='usersimpleform')
]
