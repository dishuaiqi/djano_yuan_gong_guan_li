from django.shortcuts import render,HttpResponse,redirect
from app01.models import DepartMent
from app01.models import Staff
from app01 import models
from app01.utils.pagination import Pagination  # 导入自己写的类
from app01.utils.bootstrap import BootStrapModleForm
from django import forms
from django.forms import ValidationError
from django.core.validators import RegexValidator


class Myform(BootStrapModleForm):
    class Meta:
        model=Staff
        fields=['name','password','age','salary','work_time','depart']

        # 重新定义init方法，批量设置
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
# #         循环ModelForm中的所有字段，给每个字段插件设置
#         for name,field in self.fields.items():
#             #字段中
#             field.widget.attrs={'class':'form-control'}


class MoblieForm(BootStrapModleForm):
    # 验证方式1
    telephone=forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')],
    )  #重新写了telephone的格式，用正则方式对手机号进行校验。
    class Meta:
        model=models.Preetyphone
        fields=['telephone','price','level','status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     #         循环找到所有插件，添加样式
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {'class': 'form-control'}
    #验证方式2     此方式可以很好的验证手机号是否已经存在
    def clean_telephone(self):
        txt_mobile=self.cleaned_data['telephone']
        #除自己之外，判断号码是否已存在
        exist=models.Preetyphone.objects.exclude(id=self.instance.pk).filter(telephone=txt_mobile).exists()
        if exist:
            raise ValidationError('手机号已存在')

        #验证通过,用户输入的值返回
        return txt_mobile