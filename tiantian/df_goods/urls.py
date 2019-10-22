from django.urls import path,re_path
from . import views
app_name = 'df_goods'
urlpatterns=[
    path('',views.index),
    path('index',views.index),
    re_path(r'^list(\d+)_(\d+)_(\d+)',views.list),
    #re_path(r'^detail$',views.detail),
    re_path(r'^(\d+)$',views.detail),

]

