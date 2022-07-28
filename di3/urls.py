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
from django.urls import path
from app01 import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('part/list/', views.depart_list),
    path('add/depart/', views.add_depart),
    path('del/depart/', views.del_depart),
    path('edit/depart/', views.edit_depart),
    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    # 另一种方式传id
    path('user/<int:id>/edit/', views.user_edit),
    #删除
    path('user/<int:id>/delete/', views.user_delete),

    #靓号管理
    path('mobile/list/',views.mobile_list),
    path('mobile/add/',views.mobile_add),
    path('mobile/<int:id>/edit/',views.mobile_edit),
    path('mobile/<int:id>/delete/',views.mobile_delete),

]
