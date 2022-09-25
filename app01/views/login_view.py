from django.shortcuts import redirect,render,HttpResponse
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5


class LoginForm(BootStrapForm):
    Username=forms.CharField(label='用户名',max_length=32)
    password=forms.CharField(label='密码',max_length=64,widget=forms.PasswordInput)
    def clean_password(self):
        pwd=self.cleaned_data.get('password')
        return md5(pwd)
def login(request):
    if request.method=='GET':
        form=LoginForm()
        # print(form)
        return render(request,'index.html',{'form':form})
    # print(request.POST)
    form=LoginForm(data=request.POST)
    if form.is_valid():
        user_information=form.cleaned_data
        # print('123')
        #去数据库校验密码和用户名是否正确
        admin_object=models.Admin.objects.filter(**user_information).first()

        if not admin_object:

            form.add_error('password','用户名或密码错误')
            return render(request, 'index.html', {'form': form})
        #把登录信息传进数据库
        request.session['info']={'id':admin_object.id,'name':admin_object.Username}
        return redirect('/mobile/list/')
        # return HttpResponse('提交成功')
    return render(request,'index.html',{'form':form})

'''注销'''
def logout(request):

    request.session.clear()

    return redirect('/login/')
