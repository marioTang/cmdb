# from api.base_sys import sysapi
#
import os
import sys
import json

from pyecharts import Bar
#
# #内存模块
# salt = sysapi.SaltApi()
# salt_client = "*"
# salt_method = "status.meminfo"
#
# result2 = salt.salt_command(tgt=salt_client,method=salt_method)
#
#
# SwapTotal=round(int(result2["linux-node0"]['SwapTotal']['value'])/1024,2)
# SwapFree=round(int(result2["linux-node0"]['SwapFree']['value'])/1024,2)
# MemFree=round(int(result2["linux-node0"]['MemFree']['value'])/1024,2)
# MemTotal=round(int(result2["linux-node0"]['MemTotal']['value'])/1024,2)
#
# print (SwapTotal)
# print (SwapFree)
# print (MemTotal)
# print (MemFree)
# #
# #
# # # #磁盘模块
# # salt = sysapi.SaltApi()
# # salt_client = "*"
# salt_method = "status.diskusage"
#
# result2 = salt.salt_command(tgt=salt_client,method=salt_method)
#
# grading_size=round(int(result2['linux-node0']['/']['total'])/1024/1024/1024,2)
# boot_size=round(int(result2['linux-node0']['/boot']['total'])/1024/1024/1024,2)
# home_size=round(int(result2['linux-node0']['/home']['total'])/1024/1024/1024,2)
# svwptmp_szie=round(int(result2['linux-node0']['/dev/shm']['total'])/1024/1024/1024,2)
#
# gen_available=round(int(result2['linux-node0']['/']['available'])/1024/1024/1024,2)
# boot_available=round(int(result2['linux-node0']['/boot']['available'])/1024/1024/1024,2)
# home_available=round(int(result2['linux-node0']['/home']['available'])/1024/1024/1024,2)
# swaptmp_available=round(int(result2['linux-node0']['/dev/shm']['available'])/1024/1024/1024,2)
# #
# #
# #
# #
# #
# #
# # #cpu负载
# # salt = sysapi.SaltApi()
# # salt_client = "*"
# salt_method = "status.loadavg"
#
# result2 = salt.salt_command(tgt=salt_client,method=salt_method)
#
# cpulod15_min=(result2['linux-node0']['15-min'])
# cpulod5_min=(result2['linux-node0']['5-min'])
# cpulod1_min=(result2['linux-node0']['1-min'])
#
# print (cpulod15_min)
# print (cpulod1_min)
# print (cpulod5_min)
# #
# #
# #
# # salt = sysapi.SaltApi()
# # salt_client = "*"
# # salt_method = "cmd.run"
# # args="date '+%Y-%m-%d %H:%M:%S'"
# # result2 = salt.salt_command(tgt=salt_client,method=salt_method,arg=args)
# #
# # datatime=(result2['linux-node0'])
# #
# # print (cpulod15_min)
#
# #
# # salt = sysapi.SaltApi()
# # result = salt.list_all_key()
# #
# # datatime=(result)
# # print (datatime)
# #
# # print (datatime['data']['return']['minions'])
#
#
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# render()默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，
# 设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
bar.render()