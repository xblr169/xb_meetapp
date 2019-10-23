import json
from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from app.models import User,Departs,Meetdb,Domain,Meet


def hello(request):
    return HttpResponse('hello xibei meet app')

'''
  1、部门登录
'''
def login_depart(request):
    result = "Error"
    depart = request.GET.get('depart')
    var1 = request.GET.get('var1')
    depart = Departs.objects.filter(depart=depart,var1=var1)
    if depart:
        result = "OK"
    return HttpResponse(result)


'''
 获取会议室区域信息
'''
def get_domain(request):
    domain = Domain.objects.all()
    list =[]
    for area in domain:
        area.__dict__.pop("_state")
        list.append(area.__dict__)
    return HttpResponse(json.dumps(list))

'''
  根据会议区域获取对应会议室，通过参数传递
'''
def get_room(request):
    area = request.GET.get('area')
    list = []
    if len(area):
        rooms = Meet.objects.filter(area=area)
        for room in rooms:
            room.__dict__.pop("_state")
            list.append(room.__dict__)
    return HttpResponse(json.dumps(list))

'''
  为微信息小程序提拱API以获取部门信息
'''
def get_depart(request):
    departs = Departs.objects.all()
    list = []
    # 第一种方法生成json格式:
    for depart in departs:
        depart.__dict__.pop("_state")
        list.append(depart.__dict__)
    return HttpResponse(json.dumps(list))

'''
  以list格式返回数据库查询内容
'''
def get_depart_bylist(request):
    departs = Departs.objects.all().values()
    data = {}
    data['data'] = list(departs)
    return  JsonResponse(data,safe=False)

'''
  以for循环拼接数据库查询内容为json格式
  此种方式对接微信小程序取数困难
'''
def get_depart_byjson(request):
    departs = Departs.objects.all()
    list = []
    #for 循环拼接
    for depart in departs:
        list.append([depart.code, depart.depart])
    data = {'data': list}
    return  JsonResponse(data,safe=False)

'''
 获取微信小程序POST数据以保存部门信息
'''
@csrf_exempt
def save_depart(request):
    result ="Fail"
    try:
        if request.method == 'POST':
            depart = Departs()
            received_body = request.body.decode('utf-8')
            received_body = eval(received_body)
            depart.code = received_body.get('code')
            depart.depart = received_body.get('depart')
            print(depart)
            depart.save()
            result = "OK"
            return HttpResponse(result)
    except:
        return HttpResponse(result)
