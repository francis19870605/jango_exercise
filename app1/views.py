from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user", None)
        pwd = request.POST.get("pwd", None)
        if user == "root" and pwd == "123":
            return redirect("/home/")
        else:
            error_msg = "用户或密码错误！"
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'name': '张三', 'sex': '男', 'email': 'zhangsan@123.com'},
    {'name': '李四', 'sex': '男', 'email': 'lisi@123.com'},
    {'name': '赵二', 'sex': '男', 'email': 'zhaoer@123.com'},
]

# for index in range(20):
#     temp = {'name': '王' + str(index), 'sex': '男', 'email': 'Julia@123.com'}
#     USER_LIST.append(temp)


def home(request):
    if request.method == "POST":
        home_u = request.POST.get("username", None)
        home_g = request.POST.get("gender", None)
        home_e = request.POST.get("email", None)
        tmp = {'name': home_u, 'sex': home_g, 'email': home_e}
        USER_LIST.append(tmp)
    return render(request, 'home.html', {'user_list': USER_LIST})

