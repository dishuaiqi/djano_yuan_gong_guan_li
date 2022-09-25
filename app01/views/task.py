import json
from django import forms
from django.shortcuts import render,HttpResponse

from django.views.decorators.csrf import csrf_exempt

from app01 import models

from app01.utils.bootstrap import BootStrapModleForm

from app01.utils.pagination import Pagination
class TaskModelForm(BootStrapModleForm):
    class Meta:
        model=models.Task
        fields="__all__"
        widgets={
            'detail':forms.TextInput, #正常标签
            # 'detail':forms.Textarea   #此标签比较大
        }

def task_list(request):
    '''任务列表'''
    form=TaskModelForm()
    queryset=models.Task.objects.all().order_by('-id')
    # name=models.Task.objects.filter()
    page_object = Pagination(request, queryset, page_num=2, plus=5)
    context={
        'form':form,
        'queryset':page_object.page_mobile_list,
        'page_str': page_object.html()
    }

    return render(request,'task.html',context)

@csrf_exempt
def ajax(request):
    print(request.POST)
    data_dict={'status':True,'data':[11,22,33,44]}

    json_string=json.dumps(data_dict)
    return HttpResponse(json_string)



@csrf_exempt  #免除认证
def task_add(request):
    # print(request.POST)

    #1.用户发过来的数据进行校验（ModelForm进行校验）
    form=TaskModelForm(data=request.POST)

    if form.is_valid():
        # print('123')
        form.save()
        data_dict = {'status': True}
        json_string = json.dumps(data_dict)
        return HttpResponse(json_string)
    else:
        # print(type(form.errors.as_json()))
        data_dict = {'status': False,'error':form.errors}
        json_string = json.dumps(data_dict,ensure_ascii=False)
        return HttpResponse(json_string)


