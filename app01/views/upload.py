
from django.shortcuts import render,HttpResponse,redirect
from app01.utils.bootstrap import BootStrapModleForm
from app01 import models

class upload_modalform(BootStrapModleForm):
    bootstrap_exclude_fields=['img']
    class Meta:
        model=models.City
        fields='__all__'
# def modalform(request):
#     if request.method=='GET':
#         form=upload_modalform()
#
#
#         return render(request,'file.html',{'form':form})
#     form=upload_modalform(data=request.POST,files=request.FILES)
#
#     if form.is_valid():
#         #文件自动保存上传
#         form.save()
#         return redirect('/city/list/')
#
#     return render(request,'file.html',{'form':form})


def citylist(request):
    queryset=models.City.objects.all()
    return render(request,'file.html',{'queryset':queryset})





