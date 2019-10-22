from django.urls import path,re_path
from .import views
app_name = 'df_cart'
urlpatterns=[
    path('',views.cart),
    re_path(r'^add(\d+)_(\d+)$',views.add),


]