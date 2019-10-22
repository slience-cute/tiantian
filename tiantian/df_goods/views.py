from django.shortcuts import render
from .models import *
from django.core.paginator import *
from df_user import user_decorator
# Create your views here.

def index(request):
    typelist = TypeInfo.objects.all()
    id0 = typelist[0].id
    id1 = typelist[1].id
    id2 = typelist[2].id
    id3 = typelist[3].id
    id4 = typelist[4].id
    id5 = typelist[5].id

    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:2]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:2]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:2]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:2]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:2]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:2]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:2]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:2]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:2]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:2]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:2]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:2]
    context = {"type0":type0,"type01":type01,
               "type1": type1, "type11": type11,
               "type2": type2, "type21": type21,
               "type3": type3, "type31": type31,
               "type4": type4, "type41": type41,
               "type5": type5, "type51": type51,
               "id0":id0,
               "id1": id1,
               "id2": id2,
               "id3": id3,
               "id4": id4,
               "id5": id5,

               }
    return  render(request,'df_goods/index.html',context)

#商品列表
def list(request,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    #默认 最新类排序
    if sort=='1':
        goods_list =typeinfo.goodsinfo_set.order_by('-id')
     #价格排
    if sort =='2':
        goods_list = typeinfo.goodsinfo_set.order_by('-gprice')
    #人气排
    if sort =='3':
        goods_list = typeinfo.goodsinfo_set.order_by('-gclick')

    #分页
    paginator = Paginator(goods_list,1)
    page = paginator.page(int(pindex))
    context = {"title":typeinfo.ttitle,
               "page":page,
               "paginator":paginator,
               "typeinfo":typeinfo,
               "sort":sort,
               "news":news,
    }
    return render(request,'df_goods/list.html',context)

#商品详细页
@user_decorator.login
def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('id')[0:2]
    context = {"title":goods.gtype.ttitle,
               "g":goods,
               "news":news,
               'id':id,
    }
    response =  render(request,'df_goods/detail.html',context)

    #记录最近浏览，在用户中心中使用
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_id = '%d'%goods.id
    if goods_ids!='':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>5:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids = goods_id
    response.set_cookie('goods_ids',goods_ids)
    return response


