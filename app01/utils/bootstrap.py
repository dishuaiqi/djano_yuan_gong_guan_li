'''
定义一个类，继承form.ModleForm 并把样式写好，这样在函数中可以直接继承

'''
from django import forms
class BootStrapModleForm(forms.ModelForm):
    # class Meta:
    #     model=Staff
    #     fields=['name','password','age','salary','work_time','depart']

        # 重新定义init方法，批量设置
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
#         循环ModelForm中的所有字段，给每个字段插件设置
        for name,field in self.fields.items():
            #字段中
            if field.widget.attrs:
                field.widget.attrs['class']='form-control'
                field.widget.attrs['placeholder']=field.label
            else:
                field.widget.attrs={'class':'form-control',
                                    'placeholder':field.label
                                    }

