from django.shortcuts import render,HttpResponse,redirect

from app01 import models
from app01.utils.pagination import Pagination  # 导入自己写的类

from app01.utils.forms import MoblieForm,Myform

def mobile_list(request):

    data_dict={}
    search_data=request.GET.get('q','')

    mobile_list = models.Preetyphone.objects.filter(**data_dict)

    page_object=Pagination(request,mobile_list)

    page_mobil_list=page_object.page_mobile_list


    if search_data:
        data_dict['telephone__contains']=search_data

    page_str=page_object.html()

    context={'mobil_list':page_mobil_list,  #分完页的数据
             'search_data':search_data,
             'page_str':page_str}  #页码

    return render(request,'mobile_list.html',context)





'''创建ModelForm'''



'''新增靓号'''
def mobile_add(request):

    if request.method=='GET':
        form=MoblieForm()

        return render(request,'mobile_add.html',{'form':form})
    form=MoblieForm(data=request.POST)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('/mobile/list/')

    return render(request,'mobile_add.html',{'form':form})
'''编辑靓号'''
def mobile_edit(request,id):

    # print(row_objects)
    if request.method=='GET':
        row_objects = models.Preetyphone.objects.filter(id=id).first()
        print(row_objects)

        form=MoblieForm(instance=row_objects)
        # print(form)
        return render(request,'mobile_edit.html',{'form':form})
    row_objects = models.Preetyphone.objects.filter(id=id).first()
    form=MoblieForm(data=request.POST,instance=row_objects)
    if form.is_valid():
        form.save()
        return redirect('/mobile/list/')
    return render(request,'mobile_edit.html',{'form':form})
'''删除靓号'''
def mobile_delete(request,id):
    models.Preetyphone.objects.filter(id=id).delete()
    return redirect('/mobile/list/')
