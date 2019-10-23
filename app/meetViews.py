import json
from django.views import View
from app.models import Meetdb
from django.http import  HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.response import CommonResponseMixin
from utils.dateCtrl import DateEncode
# Create your views here.

'''
 1、根据年+月获取预订信息;
'''
def get_data(request):
    if request.method =='GET':
        year = request.GET.get('year')
        month = request.GET.get('month')
        meets = Meetdb.objects.filter(year=year,month=month)
        list =[]
        for meet in meets:
            meet.__dict__.pop("_state")
            list.append(meet.__dict__)
        return HttpResponse(json.dumps(list,cls=DateEncode, ensure_ascii=False))


'''
 1、根据会议地址、会议室+月份获取预订信息;
 2、小程序列表查询界面
'''
def get_data_byamy(request):
    if request.method =='GET':
        area = request.GET.get('area')
        room = request.GET.get('room')
        month = request.GET.get('month')
        meets = Meetdb.objects.filter(area=area,meet=room,month=month).order_by('-day')
        list =[]
        for meet in meets:
            meet.__dict__.pop("_state")
            list.append(meet.__dict__)
        return HttpResponse(json.dumps(list,cls=DateEncode, ensure_ascii=False))

'''
 1、获取我的预订信息:根据用户、部门和月份获取预订信息；
 2、月份为大于等于当前月份;
'''
def get_data_byuser(request):
    list =[]
    if request.method =='POST':
        received_body = request.body
        received_body = json.loads(received_body)
        year = received_body.get('year')
        #user = received_body.get('user')
        depart = received_body.get('depart')
        month = received_body.get('month')
        meets = Meetdb.objects.filter(depart=depart, year=year).filter(month__gte=month)
        #meets = Meetdb.objects.filter(user=user, depart=depart, year=year).filter(month__gte=month)
        #打印SQL语句
        # print(str(Meetdb.objects.filter(user=user,
        #                                 depart=depart,
        #                                 year=year).filter(month__gte=month).query))
        for meet in meets:
            meet.__dict__.pop("_state")
            list.append(meet.__dict__)
    return HttpResponse(json.dumps(list, cls=DateEncode, ensure_ascii=False))

    pass

'''
 1、根据会议地址、会议室+月份获取预订信息;
'''
def get_data_byabc(request):
    list = []
    if request.method =='POST':
        received_body = request.body
        received_body = json.loads(received_body)
        year = received_body.get('year')
        area = received_body.get('area')
        room = received_body.get('room')
        month = received_body.get('month')
        meets = Meetdb.objects.filter(area=area,meet=room,year=year,month=month)
        for meet in meets:
            meet.__dict__.pop("_state")
            list.append(meet.__dict__)
    return HttpResponse(json.dumps(list,cls=DateEncode, ensure_ascii=False))


'''
1、处理小程序提交预订数据;
2、保存前判断是否有重复提交记录
'''
@csrf_exempt
def save_data(request):
    result = { }
    try:
        meetdb         = Meetdb()
        recbody        = request.body.decode('utf-8')
        recbody        = eval(recbody)
        v_year         = recbody.get('year')
        v_month        = recbody.get('month')
        v_room         = recbody.get('meet')
        v_area         = recbody.get('area')
        meetdb.open_id = recbody.get('open_id')
        meetdb.date    = recbody.get('date')
        meetdb.date2   = recbody.get('date2')
        meetdb.depart  = recbody.get('depart')
        meetdb.flag    = recbody.get('flag')
        meetdb.area    = v_area
        meetdb.meet    = v_room
        meetdb.year    = v_year
        meetdb.day     = recbody.get('day')
        meetdb.month   = v_month
        meetdb.time    = recbody.get('time')
        meetdb.user    = recbody.get('user')
        meetdb.style   = recbody.get('style')
        #=======================================================
        meet = Meetdb.objects.filter(depart=recbody.get('depart'),
                                     date=recbody.get('date'),
                                     meet=v_room)
        if meet.count():
            result = {
                'code':'-101',
                'message':'数据重复提交',
                'list':[]
            }
        else:
            meetdb.save()
            #=======返回数据;
            meets = Meetdb.objects.filter(area=v_area,meet=v_room,year=v_year, month=v_month)
            print(meets)
            list = []
            for meet in meets:
                meet.__dict__.pop("_state")
                list.append(meet.__dict__)
            result = {
                'code':'100',
                'message':'提交成功',
                'list': list
            }

    except Exception as e:
        result = {
            'code':'-500',
            'message':e.args[0],
            'list':[]
        }
    return HttpResponse(json.dumps(result,cls=DateEncode, ensure_ascii=False))

'''
  以下使用Python Mixin模式 暂未调试通
'''
class meetView(View,CommonResponseMixin):

    def get(self,request):
        pass

    '''
     保存提交的记录，主要内容有：
    '''
    @csrf_exempt
    def post(self,request):
        result ='Error:Save Data Error'
        try:
            if request.method == 'POST':
                meetdb = Meetdb()
                received_body  = request.body.decode('utf-8')
                received_body  = eval(received_body)
                meetdb.open_id = received_body.get('open_id')
                meetdb.date    = received_body.get('date')
                meetdb.date2   = received_body.get('date2')
                meetdb.depart  = received_body.get('depart')
                meetdb.flag    = received_body.get('flag')
                meetdb.area    = received_body.get('area')
                meetdb.meet    = received_body.get('meet')
                meetdb.year    = received_body.get('year')
                meetdb.day     = received_body.get('day')
                meetdb.month   = received_body.get('month')
                meetdb.time    = received_body.get('time')
                meetdb.user    = received_body.get('user')
                meetdb.style   = received_body.get('style')
                meetdb.save()
                result = 'OK: Save Data OK'
        except Exception as e:
            result = 'Error'+e.args[0]
        return HttpResponse(result)

    def put(self,request):
        pass

    def delete(self,request):
        print(request.body)
        pass

