from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from app01.models import Staff
def echart_list(request):
    return render(request,'chart_list.html')


def echart_bar(request):

    '''构造柱状图数据'''
    name=Staff.objects.all().values('name')
    legend=['狄帅旗']
    sample_list=['手机', '电脑', '电话', '充电器', '手表', '耳机']
    data_list={
        'name': legend[0],
        'type': 'bar',
        'data': [5, 20, 36, 10, 10, 20]
    }
    result={
        'status':True,
        'legend':legend,
        'xAxis':sample_list,
        'series':data_list
    }
    return JsonResponse(result)