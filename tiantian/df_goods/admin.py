from django.contrib import admin
from .models import *
# Register your models here.

#设置在管理页面中 typeinfo表显示的字段
class TypeInfoAdmin(admin.ModelAdmin):
    list_display =  ['id','ttitle']

#设置在管理页面中 GoodsInfo表显示的字段
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gkucun','gcontent','gtype','gpic']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
