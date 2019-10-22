from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from .models import *
from df_user import user_decorator
# Create your views here.

@ user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {"carts":carts}
    return render(request,'df_cart/cart.html',context)

@ user_decorator.login
def add(request,gid,count):
    # 用户uid购买了gid商品，数量为count
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    #查询购物车中是否已经有此商品，如果有数量增加，没有就新增
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)>=1:
        cart =carts[0]
        cart.count = cart.count+count

    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id'])
        return JsonResponse({"count":count})
    else:
        return  redirect('/cart')
    

