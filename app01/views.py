from django.shortcuts import render,HttpResponse,redirect
from app01.models import DepartMent
from app01.models import Staff
from app01 import models
import datetime
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

'''用户管理'''


def user_list(request):
    users=Staff.objects.all()
    # for obj in users:
        # print(obj.name,obj.password,obj.age,obj.depart_id
        #       ,obj.salary,obj.work_time.strftime('%Y-%m-%d'))

    return render(request,'user_list.html',{'users':users})


# 基于ModelForm 添加用户
from django import forms


class Myform(forms.ModelForm):
    class Meta:
        model=Staff
        fields=['name','password','age','salary','work_time','depart']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
#         循环找到所有插件，添加样式
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}



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



import random
'''展示靓号列表'''

def mobile_list(request):

    # for i in range(300):
    #     models.Preetyphone.objects.create(telephone='188'+str(random.randrange(10000000,99999999999)),price=110)


    data_dict={}
    search_data=request.GET.get('q','')

    page=int(request.GET.get('page',1))



    #每页展示个数
    page_num=15
    start_page=page_num*page-page_num
    end_page=page_num*page

    if search_data:
        data_dict['telephone__contains']=search_data



    mobil_list=models.Preetyphone.objects.filter(**data_dict)[start_page:end_page]

    total_count=models.Preetyphone.objects.filter(**data_dict).count()   #求总共有多少条数据
    # print(total_count)
    total_page,yu=divmod(total_count,page_num)       #得到整数和余数
    # print(total_page)
    # print(yu)
    if yu>0:
        total_page =total_page +1
        # print(total_page)
    '''
    自动生成页码
      <li><a href="/mobile/list/?page=1">1</a></li>
        <li><a href="/mobile/list/?page=2">2</a></li>
        <li><a href="/mobile/list/?page=3">3</a></li>
        <li><a href="/mobile/list/?page=4">4</a></li>
        <li><a href="/mobile/list/?page=5">5</a></li>
    '''
    #计算出前5页，后五页，使其在页面上显示10页
    plus=5
    #当前页小于5时
    if page<=plus:    #此判断主要用来表示当前后页小于11时，不出现负数，以及不展示没有数据的页面
        star_p=1
        end_p=2*plus+1
    else:
        #当前页>5    当前页+5>总页码
        if (page+plus)>total_page:
            star_p=total_page-2*plus
            end_p=total_page
        else:
            star_p=page-plus
            end_p=page+plus

    page_list_num=[]
    # 添加首页
    sy='<li><a href="?page={}">首页</a></li>'.format(1)
    page_list_num.append(sy)

    #添加上一页
    if page >1:
        prev= '<li><a href="?page={}">上一页</a></li>'.format(page-1)
    else:
        prev='<li><a href="?page=1">上一页</a></li>'


    page_list_num.append(prev)
    for i in range(star_p,end_p+1):
        if i ==page: #用来展示当前页

            els='<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
            els = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_list_num.append(els)

    #添加下一页
    if page <total_page:
        prev_h = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev_h = '<li><a href="?page={}">上一页</a></li>'.format(total_page)
    page_list_num.append(prev_h)
        # 添加尾页
    wy = '<li><a href="?page={}">尾页</a></li>'.format(total_page)
    page_list_num.append(wy)

    # 添加 输入页码跳转
    search_string='''
         <li>
            <form style="float: left;margin-left: -1px" method="get">
                <input name="page"
                       style="position: relative;float: left;display: inline-block;width: 88px;border-radius: 0;"
                       type="text" class="form-control" placeholder="页码">
                <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
            </form>
        </li>
    '''
    page_list_num.append(search_string)
    page_str=''.join(page_list_num)

    from django.utils.safestring import mark_safe  #需要导入这个库，标记说明此字符串是安全的，这样传入后台就可以使用了

    page_str=mark_safe(page_str)

    return render(request,'mobile_list.html',{'mobil_list':mobil_list,'search_data':search_data,'page_str':page_str})


'''创建ModelForm'''
from django.core.validators import RegexValidator

from django.forms import ValidationError
class MoblieForm(forms.ModelForm):
    # 验证方式1
    telephone=forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')],
    )  #重新写了telephone的格式，用正则方式对手机号进行校验。
    class Meta:
        model=models.Preetyphone
        fields=['telephone','price','level','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #         循环找到所有插件，添加样式
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}
    #验证方式2     此方式可以很好的验证手机号是否已经存在
    def clean_telephone(self):
        txt_mobile=self.cleaned_data['telephone']
        #除自己之外，判断号码是否已存在
        exist=models.Preetyphone.objects.exclude(id=self.instance.pk).filter(telephone=txt_mobile).exists()
        if exist:
            raise ValidationError('手机号已存在')

        #验证通过,用户输入的值返回
        return txt_mobile

'''新增靓号'''
def mobile_add(request):

    if request=='GET':
        form=MoblieForm()

        return render(request,'mobile_add.html',{'form':form})
    form=MoblieForm(data=request.POST)

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













