from django.shortcuts import render, redirect
from django.http import HttpResponse
from .base_sys import sysapi
from .base_sys import restfulapicode
from django.views import View
from api.models import systemmsg, miniondata
from django.http import JsonResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from api import models
from threading import Timer
from pyecharts import Bar
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers


class Dataview(View):
    def get(self, request):
        self.data = systemmsg.objects.all()
        try:
            salt = sysapi.SaltApi()
            salt_client = "*"
            salt_test = "test.ping"
            salt_method = "grains.items"

            result2 = salt.salt_command(salt_client, salt_method)
            for i in result2.keys():
                ipaddr = (result2[i]['ip_interfaces']["eth0"][0])
                num_cpus = (result2[i]['num_cpus'])
                osarch = (result2[i]['osarch'])
                cpumodel = (result2[i]["cpu_model"])
                osfinger = (result2[i]['osfinger'])
                hostname = (result2[i]['host'])
                nameid = (result2[i]['id'])
                kernelrelease = (result2[i]['kernelrelease'])
        except:

            return render(request, "api/sysdata.html", {"data": self.data})


        else:

            if ipaddr and num_cpus and osarch and cpumodel and osarch and hostname and kernelrelease and nameid:
                if systemmsg.objects.filter(mac_interfaces=ipaddr):

                    return render(request, "api/sysdata.html", {"data": self.data})

                else:
                    sysmsgcret = systemmsg()
                    sysmsgcret.mac_interfaces = ipaddr
                    sysmsgcret.num_cpus = num_cpus
                    sysmsgcret.osarch = osarch
                    sysmsgcret.cpu_model = cpumodel
                    sysmsgcret.osfinger = osfinger
                    sysmsgcret.hostname = hostname
                    sysmsgcret.kernelrelease = kernelrelease
                    sysmsgcret.nameid = nameid
                    sysmsgcret.save()
                    return render(request, "api/sysdata.html", {"data": self.data})


class ClientSeting(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        clienSetinmodle = systemmsg.objects.get(mac_interfaces=request.POST.get('mac_interfaces'))
        clienSetinmodle.mac_interfaces = request.POST.get("mac_interfaces")
        clienSetinmodle.osfinger = request.POST.get("osfinger")
        clienSetinmodle.osarch = request.POST.get("osarch")
        clienSetinmodle.kernelrelease = request.POST.get("kernelrelease")
        clienSetinmodle.cpu_model = request.POST.get("cpu_model")
        clienSetinmodle.num_cpus = request.POST.get("num_cpus")
        clienSetinmodle.mac_interfaces = request.POST.get("mac_interfaces")
        clienSetinmodle.hostname = request.POST.get("hostname")
        clienSetinmodle.save()

        return JsonResponse({'code': '200', 'text': 'SUCCESS', 'result': None, })


class Fenye(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        book_list = systemmsg.objects.all()

        # 创建分页器对象,每页显示15条
        paginator = Paginator(book_list, 10)
        # 从请求中获取页码,page=0,就默认显示第一页
        page = request.GET.get('page', 1)
        # 获取当前页
        currentPage = int(page)

        # 如果页数十分多时，换另外一种显示方式
        # 如果页面总数大于n页
        if paginator.num_pages > 6:

            if currentPage - 5 < 1:
                pageRange = range(1, 11)
            elif currentPage + 5 > paginator.num_pages:
                pageRange = range(currentPage - 5, paginator.num_pages + 1)

            else:
                pageRange = range(currentPage - 5, currentPage + 5)

        else:
            pageRange = paginator.page_range

        try:
            #print(page)
            book_list = paginator.page(page)
        except PageNotAnInteger:
            book_list = paginator.page(1)
        except EmptyPage:
            book_list = paginator.page(paginator.num_pages)
        return render(request, 'api/fenye.html', locals())

    def post(self, request):
        aaaaaa = request.POST.get("aaaa")
        print (aaaaaa)
        book_list = systemmsg
        host=serializers.serialize("json",book_list.objects.filter(mac_interfaces=request.POST.get("aaaa")))
        # print (restfulapicode.cdoe_status404)
        return JsonResponse(host,safe=False)






class Miniondata(View):
    def get(self, request):
        hostname=request.GET.get('nameid')

        def sysdata():
            salt = sysapi.SaltApi()
            result2 = salt.salt_command(tgt=hostname, method="status.meminfo")
            SwapTotal = float(round(int(result2[hostname]['SwapTotal']['value']) / 1024, 2))
            SwapFree = float(round(int(result2[hostname]['SwapFree']['value']) / 1024, 2))
            MemFree = float(round(int(result2[hostname]['MemFree']['value']) / 1024, 2))
            print (MemFree)
            MemTotal = float(round(int(result2[hostname]['MemTotal']['value']) / 1024, 2))


            result3 = salt.salt_command(tgt=hostname, method="status.diskusage")

            grading_size = float(round((result3[hostname]['/']['total']) / 1024 / 1024 / 1024, 2))
            boot_size = float(round((result3[hostname]['/boot']['total']) / 1024 / 1024 / 1024, 2))
            home_size = float(round((result3[hostname]['/home']['total']) / 1024 / 1024 / 1024, 2))
            swaptmp_szie = float(round((result3[hostname]['/dev/shm']['total']) / 1024 / 1024 / 1024, 2))
            gen_available = float(round((result3[hostname]['/']['available']) / 1024 / 1024 / 1024, 2))
            boot_available = float(round((result3[hostname]['/boot']['available']) / 1024 / 1024 / 1024, 2))
            home_available = float(round((result3[hostname]['/home']['available']) / 1024 / 1024 / 1024, 2))
            swaptmp_available = float(round((result3[hostname]['/dev/shm']['available']) / 1024 / 1024 / 1024, 2))

            result4 = salt.salt_command(tgt=hostname, method="status.loadavg")
            cpulod15_min = float(result4[hostname]['15-min'])
            cpulod5_min = float(result4[hostname]['5-min'])
            cpulod1_min = float(result4[hostname]['1-min'])

            minionmodel = models.miniondata()
            minionmodel.SwapTotal = SwapTotal
            minionmodel.SwapFree = SwapFree
            minionmodel.MemFree = MemFree
            minionmodel.SwapFree = SwapFree
            minionmodel.MemTotal = MemTotal
            minionmodel.grading_size = grading_size
            minionmodel.boot_size = boot_size
            minionmodel.home_szie = home_size
            minionmodel.swaptmp_szie = swaptmp_szie

            minionmodel.gen_available = gen_available
            minionmodel.boot_available = boot_available
            minionmodel.home_available = home_available
            minionmodel.swaptmp_available = swaptmp_available
            minionmodel.cpulod15_min = cpulod15_min
            minionmodel.cpulod5_min = cpulod5_min
            minionmodel.cpulod1_min = cpulod1_min
            minionmodel.save()
            t = Timer(10, sysdata)
            t.start()

        sysdata()
        listhost=models.systemmsg.objects.filter(nameid=hostname)
        return render(request, 'api/minlondata.html', {"data": listhost})



class Test(View):

    def get(self,request):
        from pyecharts import Pie
        REMOTE_HOST = "https://pyecharts.github.io/assets/js"

        def Pie_(self):

            attr = ["衬衫", "ttrr", "雪纺衫", "裤子", "高跟鞋", "袜子"]
            v1 = [11, 12, 13, 10, 10, 10]
            pie = Pie("磁盘数据")
            pie.width: str="700px"
            pie.height: str="300px"
            pie.add("", attr, v1, is_label_show=True)
            return pie



        # 可视化展示页面
        pie = Pie_(self)
        myechart = pie.render_embed()  # 饼图
        host = REMOTE_HOST  # js文件源地址
        script_list = pie.get_js_dependencies()  # 获取依赖的js文件名称（只获取当前视图需要的js）
        return render(request, "api/tu.html", {"myechart": myechart, "host": host, "script_list": script_list})



        # host = "https://pyecharts.github.io/assets/js"
        #
        #
        # bar = Bar("我的第一个图表", "这里是副标题")
        # bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
        # qq=bar
        # print (qq)
        # script_list=bar.get_js_dependencies()
        # return render(request, 'api/sysdata.html', {"myechart": qq, "host": host, "script_list": script_list} )




