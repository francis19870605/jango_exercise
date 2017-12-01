from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

USER_LIST = [
    {'name': '王', 'sex': '男', 'email': 'Julia@123.com'},
]

for index in USER_LIST:
    temp = {'name': '王'+str(index), 'sex': '男', 'email': 'Julia@123.com'}
    USER_LIST.append(temp)

def login(request):
    user = request.POST.get("user", None)
    pwd = request.POST.get("pwd", None)
    if user == "root" and pwd == "123":
        return redirect("/home/")
    else:
        error_msg = "用户或密码错误！"
    return render(request, 'login.html', {'error_msg': error_msg})
