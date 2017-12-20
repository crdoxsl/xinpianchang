from django.shortcuts import render
from .forms.register import RegisterForm
from App.models import User
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'App/home.html')
def Register(request):
    if request.method == 'GET':
        f = RegisterForm()
    if request.method == 'POST':
        print('*'*50)
        f = RegisterForm(request.POST)
        print('22222222222222')

        if f.is_valid():
            print('333333333333')
            data = f.cleaned_data
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            print('111111111111111')
            User.objects.create(username=username,password=password,email=email)
            print('66666666666666666')
            return HttpResponse('注册成功')
        else:
            errors = f.errors
            print(errors)
            # return (request,'App/register.html', {'form':f})

    return render(request, 'App/register.html', {'form': f})
    # if request.method == 'GET':
    #     f = RegisterForm()
    #     return render(request,'App/register.html', {'form':f})

def Video(request):
    return  render(request, 'App/video.html')
