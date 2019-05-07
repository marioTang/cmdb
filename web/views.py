from django.shortcuts import render
from web import models
from web.models import user
from django.contrib.auth import login, logout

from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return  render(request, 'user/index.html')

def host(request):
    return  render(request, 'user/host.html')


def getall(request):
    getkey_all= models.sysmsg.objects.all()                      #查询所有
    return render(request, "user/host.html", {'getkey_all': getkey_all})


#用户验证
def login(request):
    if request.method == "POST":
        userid = request.POST.get('user', None)
        password = request.POST.get('passwd', None)

        print (userid)
        print (password)

        if userid and password:  # 确保用户名和密码都不为空
                # username = user.strip()
                # 用户名字符合法性验证
                # 密码长度验证
                # 更多的其它验证....
                try:
                    user = models.user.objects.get(username=userid)
                    if user.password == password:
                        return render(request, "user/index.html")
                    else:
                        message = "密码不正确！"
                        return render(request, 'user/login.html', {"message": message})
                except:
                    message = "用户名不存在！"
                    return render(request, 'user/login.html', {"message": message})
    return render(request, 'user/login.html')




def register(request):
    if request.method=="GET":
        return  render(request, "user/register.html")

#用户展示
def users(request):
    if request.method=="GET":
        userall=models.user.objects.all()
        return  render(request, "user/user.html", {'userall' : userall})


#用户删除
def deluser(request):
    if request.method=="GET":
        getid=request.GET.get('id')
        models.user.objects.filter(id=getid).delete()
        userall = models.user.objects.all()
        return render(request, "user/user.html", {'userall': userall})


#用户修改
def edituser(request):

    if request.method == "GET":
        editid=request.GET.get('id')
        userall=models.user.objects.get(id=editid)
        return render(request, "user/edituser.html", {'userall' : userall})

    elif request.method == "POST":
         name = request.POST.get("name", None)
         passwd = request.POST.get("password", None)
         telphone = request.POST.get("telphone", None)
         editid = request.POST.get("id", None)
         email = request.POST.get("email", None)


         if name and passwd and telphone and editid and email:
            usermod = models.user.objects.get(id=editid)
            usermod.username = request.POST.get('name', '').strip()
            usermod.password = request.POST.get('password', '').strip()
            usermod.telephone = request.POST.get('telphone', '').strip()
            usermod.email = request.POST.get('email', '').strip()

            usermod.save()
            message = "用户修改成功！"
            return render(request, "user/edituser.html", {'message': message})
         else:
            message = "表单为空! 请重新提交"
            return render(request, "user/edituser.html", {'message': message})



def edituserdata(request):
    # if request.method=="POST":
    #     name=request.POST.get("name")
    #     passwd=request.POST.get("password")
    #     email=request.POST.get("email")
    #     telphone=request.POST.get("telphone")
    #     print(name)
    #     print(passwd)
    #     print(email)
    return render(request, "user/index.html")


def logouts(request):
    logout(request)

    return render(request, "user/login.html")

