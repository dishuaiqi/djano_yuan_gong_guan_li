from app01.models import Admin
from django.shortcuts import redirect,render,HttpResponse
from app01.utils.pagination import Pagination
from app01.utils.forms import AdminForm
def admin_list(request):
    adminlist=Admin.objects.all()
    page_object=Pagination(request,mobile_list=adminlist)

    context={
        'adminlist': adminlist,
         'queryset':page_object.page_mobile_list,
         'page_str':page_object.html()
    }
    return render(request,'admin_list.html',context)


def admin_add(request):

    if request.method == 'GET':
        form =AdminForm()

        return render(request, 'admin_add.html', {'form': form})
    form = AdminForm(data=request.POST)
    # print(form)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'admin_add.html', {'form': form})

def admin_edit(request,id):
    if request.method == 'GET':
        row_objects = Admin.objects.filter(id=id).first()
        # print(row_objects)

        form = AdminForm(instance=row_objects)
        # print(form)
        return render(request, 'admin_edit.html', {'form': form})
    row_objects = Admin.objects.filter(id=id).first()
    form = AdminForm(data=request.POST, instance=row_objects)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'admin_edit.html', {'form': form})