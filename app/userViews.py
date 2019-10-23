import json
from django.views import View
from app.models import User
from django.http import  HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.response import CommonResponseMixin
from utils.dateCtrl import DateEncode

def get_user(request):
    try:
        if request.method == 'GET':
            depart = request.GET.get('depart')
            if depart != None:
                if depart =='请选择':
                    users = User.objects.all()
                else:
                    users = User.objects.filter(depart=depart)
            else:
                users = User.objects.all()
            list =[]
            for user in users:
                user.__dict__.pop("_state")
                list.append(user.__dict__)
            return HttpResponse(json.dumps(list))
    except Exception as e:
        return HttpResponse(e.args[0])

'''
  系统登录信息
'''
def login(request):
     usercode = request.GET.get('code')
     user = User.objects.filter(user_code=usercode)
     list =[]
     for usr in user:
         usr.__dict__.pop("_state")
         list.append(usr.__dict__)
     return HttpResponse(json.dumps(list))

'''
  json提交的数据保存登录用户信息
'''
@csrf_exempt
def save_user(request):
    result = 'Error'
    try:
        if request.method =='POST':
            user = User()
            received_body = request.body.decode('utf-8')
            received_body = eval(received_body)
            user.user_code = received_body.get('usercode')
            user.user_name = received_body.get('username')
            user.depart = received_body.get('depart')
            user.password = received_body.get('password')
            user.open_id = received_body.get('open_id')
            user.save()
            result ='OK'
    except Exception as e:
        result = 'Error'+ e.args[0]
    return HttpResponse(result)


class userView(View):

    def get(self, request):
        try:
            usercode = request.GET.get('code')
            if usercode:
                users = User.objects.filter(user_code=usercode)
            else:
                users = User.objects.all()
            list = []
            for user in users:
                user.__dict__.pop("_state")
                list.append(user.__dict__)
            return HttpResponse(json.dumps(list))
        except Exception as e:
            return HttpResponse(e.args[0])


    def post(self, request):
        result = 'Error'
        try:
            if request.method == 'POST':
                user = User()
                received_body = request.body.decode('utf-8')
                received_body = eval(received_body)
                user.user_code = received_body.get('usercode')
                user.user_name = received_body.get('username')
                user.depart = received_body.get('depart')
                user.password = received_body.get('password')
                user.open_id = received_body.get('open_id')
                user.save()
                result = 'OK'
        except Exception as e:
            result = 'Error' + e.args[0]
        return HttpResponse(result)

    #删除记录;
    def delete(self, request):
        result = 'Error'
        id = request.GET.get('user')
        user = User.objects.filter(user_id=id)
        if user:
            user.delete()
            result = 'OK'
        print(id)
        return HttpResponse(result)

