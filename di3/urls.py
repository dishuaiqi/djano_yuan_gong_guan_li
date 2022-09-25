"""di3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from app01.views import depart,mobile,staff,AdminView,login_view,task,order,echart,upload
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    path('part/list/', depart.depart_list),
    path('add/depart/', depart.add_depart),
    path('del/depart/', depart.del_depart),
    path('edit/depart/', depart.edit_depart),
    # 用户管理
    path('user/list/', staff.user_list),
    path('user/add/', staff.user_add),
    # 另一种方式传id
    path('user/<int:id>/edit/', staff.user_edit),
    #删除
    path('user/<int:id>/delete/', staff.user_delete),

    #靓号管理
    path('mobile/list/',mobile.mobile_list),
    path('mobile/add/',mobile.mobile_add),
    path('mobile/<int:id>/edit/',mobile.mobile_edit),
    path('mobile/<int:id>/delete/',mobile.mobile_delete),

    #登录用户管理
    path('admin/list/',AdminView.admin_list),
    path('admin/add/',AdminView.admin_add),
    path('admin/<int:id>/edit/',AdminView.admin_edit),

    #登录
    path('login/',login_view.login),
    path('logout/',login_view.logout),


#     任务管理
    path('task/list/',task.task_list),
    path('task/ajax/',task.ajax),
    path('task/add/',task.task_add),


    #订单管理
    path('order/list/',order.order_list),
    path('order/add/',order.order_add),
    path('order/delete/',order.order_delete),
    path('order/edit/',order.order_edit),

    #图表管理
    path('echart/list/',echart.echart_list),
    path('echart/bar/',echart.echart_bar),

    #上传管理
    # path('upload/modal/form/',upload.modalform),
    path('city/list/',upload.citylist),

]
