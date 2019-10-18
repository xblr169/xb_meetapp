import  json
from django.http import HttpResponse,JsonResponse
from django.views import View
from app.models import Meetdb
from django.views.decorators.csrf import csrf_exempt

'''
1、自定义类继承自View
2、测试客户端请求的get\post\put\delete方法；
'''
class meview(View):
    def get(self,request):
        return HttpResponse('This is request get method')

    def post(self,request):
        print(request.method)
        result ={
            'message': 'post method success.',
            'code':'200'
        }
        return JsonResponse(data=result,safe=False)


    def put(self,request):
        return HttpResponse('This is request put method')

    #删除记录;
    def delete(self,request):
        result ='Error'
        id = request.GET.get('id')
        meetdb = Meetdb.objects.filter(meet_id=id)
        print('2222',len(meetdb))
        if meetdb:
            meetdb.delete()
            result = 'OK'
        print(id)
        return HttpResponse(result)