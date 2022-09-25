import json
import random
from datetime import datetime
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from app01.utils import pagination
from app01 import models

from app01.utils.bootstrap import BootStrapModleForm
from django.views.decorators.csrf import csrf_exempt



class OrderModelForm(BootStrapModleForm):
    class Meta:
        model=models.Order
        # fields = '__all__'
        fields=['title','price','status'] #表示展示哪些字段

        # exclude=['order_number']  #表示排除哪些字段

def order_list(request):

    form=OrderModelForm()
    queryset=models.Order.objects.all().order_by('-id')
    page_object=pagination.Pagination(request,queryset,page_num=6, plus=5)
    context={
        'form':form,
        'queryset': page_object.page_mobile_list,
        'page_str': page_object.html()
    }
    return render(request,'order_list.html',context)


@csrf_exempt
def order_add(request):

    form=OrderModelForm(data=request.POST)

    if form.is_valid():
        #让订单号自动生成
        form.instance. order_number=str(datetime.now().strftime('%Y%m%d%H%M%S')+str(random.randint(10,99)))
        #让管理员自动添加
        form.instance.admin_id=request.session['info']['id']
        form.save()

        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})

def order_delete(request):
    uid=request.GET.get('uid')
    # print(uid)
    models.Order.objects.filter(id=uid).delete()

    return JsonResponse({'status':True})


def order_edit(request):
    uid=request.GET.get('uid')

    res_data=models.Order.objects.filter(id=uid).first()
    data_status={
        'title':res_data.title,
        'price':res_data.price,
        'status':res_data.status,
    }
    return JsonResponse(data_status)