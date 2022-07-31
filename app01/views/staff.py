from django.shortcuts import render,HttpResponse,redirect

from app01.models import Staff

from app01.utils.pagination import Pagination  # 导入自己写的类

from app01.utils.forms import MoblieForm,Myform

def user_list(request):
    users=Staff.objects.all()
    mobile_list=users
    page_object=Pagination(request,mobile_list,page_num=2,plus=5)
    # for obj in users:
        # print(obj.name,obj.password,obj.age,obj.depart_id
        #       ,obj.salary,obj.work_time.strftime('%Y-%m-%d'))
    context={
        'users':page_object.page_mobile_list,
        'page_str':page_object.html()
    }

    return render(request,'user_list.html',context)


# 基于ModelForm 添加用户


def user_add(request):
    if request.method=='GET':
        form=Myform()


        return render(request,'user_add.html',{'form':form})
#     获取数据以及校验 和单个数据也是不一样的
#     print(request.POST)
    form=Myform(data=request.POST)
#     判断数据是否合法，保存到数据库
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list')
    # 校验失败，会把错误信息传到页面上
    return render(request,'user_add.html',{'form':form})


def user_edit(request,id):

    if request.method=='GET':

        row_object=Staff.objects.filter(id=id).first()    #获取当前id的那一行数据

        print(row_object)
        form=Myform(instance=row_object)     #把获取的值通过instace参数传入form中



        return render(request,'user_edit.html',{'form':form})

    row_object=Staff.objects.filter(id=id).first()
    form=Myform(data=request.POST,instance=row_object)  #更新这一行的数据
    # print(request.POST)
    # print(row_object)
    if form.is_valid():

        form.save()
        return redirect('/user/list')
    # 校验失败，会把错误信息传到页面上
    return render(request,'user_edit.html',{'form':form})


'''删除'''
def user_delete(request,id):

    Staff.objects.filter(id=id).delete()

    return redirect('/user/list/')
