from django import forms
# from respository import models
# from werkzeug.routing import ValidationError
from django.core.exceptions import ValidationError

from App.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=6, required=True, error_messages={"required": '用户名不能为空', "invalid": '格式错误'}, widget=forms.TextInput)
    password = forms.CharField(max_length=50, min_length=6, required=True, error_messages={"required": '密码不能为空', "invalid": '格式错误'}, widget=forms.PasswordInput)
    email = forms.EmailField(required=True, error_messages={"required": '邮箱不能为空', "invalid": '格式错误'}, widget=forms.EmailInput)

    #
    # def clean_username(self):

# username = self.cleaned_data.get('username')
#     users = User.objects.filter(username = username).count()
#     if users:
#         raise ValueError('用户名已存在')
#     return username

    def clean_username(self):
        # 对username的扩展验证，查找用户是否已经存在
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username).count()
        if users:
            raise ValidationError('用户已经存在！')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_count = User.objects.filter(email=email).count()
        if email_count:
            raise ValidationError('该邮箱已经注册')
        return email

