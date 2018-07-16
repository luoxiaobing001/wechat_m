from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response

from .models import Department, Position, Content, AreaInfo,WechatInfo, User
from django.http import JsonResponse,HttpResponse
from django.db.models import Sum

#数据可视化
from django.template import loader
#文件上传
from django import forms

import datetime

# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)
        #print('i am %s' % user)

        if user:
            request.session['uid'] = user.id
            request.session['uname'] = user.real_name
            request.session['position'] = user.position.name
            # print(user[0].id)
            return HttpResponseRedirect('/')

            # return render_to_response('main.html', {'user': user})
        else:
            return render(request, 'signin.html', {'login_error': '用户名或密码错误'})  # 登录失败

    elif request.method == 'GET':
        return render(request, 'signin.html', {'login_error': ''})

def login_requered(func):
    def check_login_status(request):
        if request.session.has_key('uid'):
            return func(request)
        else:
            return HttpResponseRedirect('login/')
    return check_login_status

def logout(request):
    del request.session['uid']
    return redirect(login)

@login_requered
def index(request):
    if request.method == 'GET':
        user_id = request.session.get('uid')
        user = User.objects.get(id=user_id)
        return render(request, 'main.html', {'user': user})
    if request.method == 'POST':
        province_id = int(request.POST.get('province'))
        city_id = int(request.POST.get('city', None))
        county_id = int(request.POST.get('county', None))
        if county_id == -1 and city_id != -1:
            area_id = city_id
        elif city_id == -1 and province_id != -1:
            area_id = province_id
        elif county_id != -1:
            area_id = county_id
        else:
            error_msg ='未选择区域'
        area_info = AreaInfo.objects.get(id=area_id)

        user_id = request.session['uid']
        user = User.objects.get(id=user_id)

        wechat_id = request.POST.get('wechat_id', None)
        original_fans_num = int(request.POST.get('original_fans', None))
        add_fans_type = int(request.POST.get('add_fans_type', None))
        today_fans_num = int(request.POST.get('today_fans_num', None))
        if add_fans_type == 1:
            passive_fans_num = today_fans_num
            active_fans_num = 0
        elif add_fans_type == 2:
            passive_fans_num = 0
            active_fans_num = today_fans_num

        send_invited_num = int(request.POST.get('send_invited_num', None))
        dialog_num = int(request.POST.get('dialog_num', None))
        send_zone_num = int(request.POST.get('send_zone_num', None))
        group_add_num = int(request.POST.get('group_add_num', None))
        send_zone_for_friend_num = int(request.POST.get('send_zone_for_friend_num', None))

        articleAdd = Content.objects.create(wechat_id=wechat_id, user=user, area_info=area_info, original_fans_num=original_fans_num,
                                            passive_fans_num=passive_fans_num, active_fans_num=active_fans_num, send_invited_num=send_invited_num, dialog_num=dialog_num,
                                            send_zone_num=send_zone_num, group_add_num=group_add_num, send_zone_for_friend_num=send_zone_for_friend_num)
        if articleAdd:
            return render(request, 'main.html', {'msg':'保存成功!'})
        else:
            return render(request, 'main.html', {'msg':'保存失败!'})
        return render(request, 'main.html')


def regist(request):
    # if request.method == 'POST':
    #     uf = UserForm(request.POST)  # 包含用户名和密码
    #     if uf.is_valid():
    #         # 获取表单数据
    #         username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
    #         password = uf.cleaned_data['password']
    #         # 添加到数据库
    #         # registAdd = User.objects.get_or_create(username=username,password=password)
    #         registAdd = User.objects.create_user(username=username, password=password)
    #         # print registAdd
    #         if registAdd == False:
    #             return render(request, 'share1.html', {'registAdd': registAdd, 'username': username})
    #
    #         else:
    #             # return HttpResponse('ok')
    #             return render(request, 'share1.html', {'registAdd': registAdd})
    #             # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    # else:
    #     # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
    #     uf = UserForm()
    # # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    # return render(request, 'regist1.html', {'uf': uf})
    pass


# 获取省数据
def getProvince(request):
    provinceList = AreaInfo.objects.filter(parent_id=0)
    # print(provinceList)
    list1 = []
    for item in provinceList:
        list1.append([item.id, item.name])
    return JsonResponse({'data': list1})

# 获取市数据
def getCity(request, pid):
    cityList = AreaInfo.objects.filter(parent_id=pid)
    list1 = []
    for item in cityList:
        list1.append([item.id, item.name])
    return JsonResponse({'data': list1})

# 获取县数据
def getCounty(request, cid):
    countyList = AreaInfo.objects.filter(parent_id=cid)
    # print(countyList)
    list1 = []
    for item in countyList:
        list1.append([item.id, item.name])
    return JsonResponse({'data': list1})


# 获取县数据
def getDepartment(request):
    departmentList = Department.objects.all()
    list1 = []
    for item in departmentList:
        list1.append([item.id, item.name])
    return JsonResponse({'data': list1})

# 获取县数据
def getPosition(request):
    positionList = Position.objects.all()
    list1 = []
    for item in positionList:
        list1.append([item.id, item.name])
    return JsonResponse({'data': list1})


from functools import reduce

@login_requered
def modify(request):
    user_id = request.session.get('uid')
    user = User.objects.get(id=user_id)
    return render(request, 'modify_data.html', {'user': user})

#处理二维码上传
class WechartForm(forms.Form):
    wechatId = forms.CharField(label='微信ID', max_length=200)
    QRCode = forms.ImageField(label='二维码')

@login_requered
def account(request):
    #刚显示时调用GET方法
    if request.method=="POST":
        wf = WechartForm(request.POST,request.FILES)#刚显示时，实例化表单（是否有数据）
        if wf.is_valid():#验证数据是否合法，当合法时可以使用cleaned_data属性。
            #用来得到经过'clean'格式化的数据，会所提交过来的数据转化成合适的Python的类型。
            wechatId = wf.cleaned_data['wechatId']
            QRCode = wf.cleaned_data['QRCode']
            #write in database
            wi=WechatInfo()#实例化wi对象
            wi.wechatId = wechatId
            wi.QRCode = QRCode
            wi.save()#保存到数据库表中
            return HttpResponse('上传成功!')#重定向显示内容（跳转后内容）
    else:
        wf=WechartForm()#刚显示时，实例化空表单
    user_id = request.session.get('uid')
    user = User.objects.get(id=user_id)
    return render(request, 'account_entry.html',{'wf': wf, 'user': user})#只有刚显示时才起作用

@login_requered
def personal_week_chart(request):
    '''个人本周数据统计'''
    user_id = request.session.get('uid')
    user = User.objects.get(id=user_id)

    lstX = []
    lstY = []
    # 获取数据

    contents = Content.objects.filter(user_id=user.id).values('create_date').annotate(sum_fans=Sum('passive_fans_num')).values('create_date', 'sum_fans')

    for content in contents:
        lstX.append(content['create_date'].strftime('%Y-%m-%d'))
        lstY.append(content['sum_fans'])
    print(lstX,lstY)
    return render(request, 'personal_week_chart.html',{'user': user, 'X':lstX, 'Y': lstY})

def group_week_chart(request):
    '''每组本周数据统计'''
    user_id = request.session.get('uid')
    user = User.objects.get(id=user_id)

    lstX = []
    lstY = []
    # 获取数据

    contents = Content.objects.filter(user_id=user.id).values('create_date').annotate(
        sum_fans=Sum('passive_fans_num')).values('create_date', 'sum_fans')

    for content in contents:
        lstX.append(content['create_date'].strftime('%Y-%m-%d'))
        lstY.append(content['sum_fans'])
    print(lstX, lstY)
    return render(request, 'group_week_chart.html', {'user': user, 'X': lstX, 'Y': lstY})

def people_day_chart(request):
    '''所有人当日数据对比'''
    #罗孝兵
    user_id = request.session.get('uid')
    user = User.objects.get(id=user_id)

    lstX = []
    lstY = []
    # 获取数据

    contents = Content.objects.filter(create_date=datetime.date.today()).annotate(
        sum_fans=Sum('passive_fans_num')).values('user__real_name', 'sum_fans')

    for content in contents:
        lstX.append(content['user__real_name'])
        lstY.append(content['sum_fans'])
    print(lstX, lstY)
    return render(request, 'people_day_chart.html', {'user': user, 'X': lstX, 'Y': lstY})