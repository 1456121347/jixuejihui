from django.urls import path,include,re_path

import xadmin

from django.views.generic import TemplateView
# from users.views import user_login
from users.views import LoginView,logout_view,RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    # path('login', TemplateView.as_view(template_name='login.html'),name='login'),
    # path('login/',user_login,name='login'),     #修改login路由
    #登录
    path('login/',LoginView.as_view(),name='login'),
    #登出
    path('logout/',logout_view,name='logout'),
    #注册
    path('register/',RegisterView.as_view(),name='register'),
    #验证码
    path('captcha/',include('captcha.urls')),
    # 激活
    re_path('active/(?P<active_code>.*)',ActiveUserView.as_view(), name='active_code'),
    #找回密码
    path('forgetpwd/',ForgetPwdView.as_view(),name='forgetpwd'),
    #处理重置密码的链接
    re_path('reset/(?P<active_code>.*)/',ResetPwdView.as_view(),name='reset_pwd'),
    # 重置密码
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),

]
