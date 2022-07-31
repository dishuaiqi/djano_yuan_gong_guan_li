from django.shortcuts import render,HttpResponse,redirect
from app01.models import DepartMent

''' 部门管理'''
def depart_list(request):
    part_list=DepartMent.objects.all()

    return render(request,'depart_list.html',{'part_list':part_list})

'''              添加表格的内容          '''
def add_depart(request):
    # DepartMent.objects.create(title='运营部')

    if request.method=='GET':


        return render(request,'add_part.html')
    title=request.POST.get('title')


    DepartMent.objects.create(title=title)

    return redirect('/part/list/')


'''              删除表格中的内容                 '''
def del_depart(request):
    nid=request.GET.get('nid')
    print(nid)
    DepartMent.objects.filter(id=nid).delete()
    return redirect('/part/list/')


'''                   修改表格                   '''
def edit_depart(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        yuan_title=DepartMent.objects.filter(id=nid).first().title
        return render(request,'edit_depart.html',{'yuan_title':yuan_title})
    title=request.POST.get('title')
    nid = request.GET.get('nid')
    DepartMent.objects.filter(id=nid).update(title=title)
    return redirect('/part/list/')