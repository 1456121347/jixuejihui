from  django import forms
from captcha.fields import CaptchaField
#登录表单验证
class LoginForm(forms.Form):
    #用户名.密码不能为空 切密码不能小于6位
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,max_length=6)

#注册表单验证
class RegisterForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=6)
    captcha = CaptchaField(error_messages={'invalid':"验证码错误"})

# 忘记密码表单验证
class ForgetPwdForm(forms.Form):
    email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid':"验证码错误"})




# 重置密码的表单验证
class ModifyPwdForm(forms.Form):
    email = forms.CharField(required=True,error_messages={'invalid':"邮箱错误"})
    password1 = forms.CharField(required=True,min_length=6,error_messages={'invalid':"pwd1输入错误"})
    password2 = forms.CharField(required=True,min_length=6,error_messages={'invalid':"pwd2输入错误"})


