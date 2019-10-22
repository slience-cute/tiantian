from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import UserInfo
import sys
import os
sys.path.append("../")
from df_goods import models
from hashlib import sha1
from . import user_decorator
# Create your views here.

#注册
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    # 接受用户注册信息
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    uemail = request.POST.get('email')
    if upwd!=cpwd:
        return HttpResponseRedirect('/user/register')
    else:

        user = UserInfo()
        user.uname = uname
        sha = sha1(upwd.encode('utf-8'))
        upwd1 = sha.hexdigest()
        user.upwd = upwd1
        user.uemail = uemail
        user.save()
        return HttpResponseRedirect('/user/login')
#登录
def login(request):
    uname=request.COOKIES.get('uname','')
    context={'error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

#退出：
def logout(request):
    del request.session['user_id']
    return redirect('/goods/index')


#判断用户名是否存在：
def register_exist(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(uname=name).count()
    return JsonResponse({"count":count})

#登录检测
def login_handle(request):
    #接受登录信息
    post= request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu =post.get('jizhu',0)
    #根据用户名查询对象
    users= UserInfo.objects.filter(uname=uname)
    print(uname)
    #判断：如果未查到则用户名错，如果查到就判断密码是否正确，正确就转到用户中兴
    if len(users)==1:
        sha=sha1(upwd.encode('utf-8'))
        upwd1=sha.hexdigest()
        if upwd1==users[0].upwd:
            red = HttpResponseRedirect('/user/info')
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'error_name':0,'error_pwd':1,"uname":uname,"upwd":upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'error_name':1,'error_pwd':0,"uname":uname,"upwd":upwd}
        return  render(request,'df_user/login.html',context)

#用户中心：
@user_decorator.login
def info(request):
    uemail = UserInfo.objects.get(id=request.session['user_id']).uemail
    uname=UserInfo.objects.get(id=request.session['user_id']).uname
    #最近浏览
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    if goods_ids=='':
        explain = 0
    else:
        explain = 1
        for goods_id  in  goods_ids1:
            goods_list.append(models.GoodsInfo.objects.get(id=int(goods_id)))

    context = {'uname':uname,'uemail':uemail,'goods_list':goods_list,"explain":explain}
    return render(request,'df_user/user_center_info.html',context)


#订单
@user_decorator.login
def order(request):
    return render(request,'df_user/user_center_order.html')


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post = request.POST
        user.ushou=post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user':user}
    return  render(request,'df_user/user_center_site.html',context)















