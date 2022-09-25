from django.utils.deprecation import MiddlewareMixin   #应用Django自带的库来写新的中间件

from django.shortcuts import render,redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        #判断是哪个界面 如果是登录界面，就不进行重定向
        if request.path_info=='/login/':
            return

        #找到登录信息
        info_dirct=request.session.get('info')
        #如果存在，就进继续 否则返回登录界面
        if info_dirct:
            return
        return redirect('/login/')