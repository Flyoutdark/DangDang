from django.contrib import admin
from django.urls import path, include
from robot_app import views

urlpatterns = [
    path('regist/', views.regist),#注册路径
    path('login/', views.login),#登录路径
    path('main/', views.main_page),#主页显示
    path('introduce/', views.introduce),
    path('menu/', views.menu_page),
    path('authcode/', views.auth_code),#登录验证码
    path('registlogic/',views.regist_logic,name='reglogic'),
    path('registajax/',views.Reggist_Ajax,name='regajax'),#注册信息的异步验证
    path('sendcode/',views.SendCode,name='sendcode'),#发送激活码给用户
    path('jhcode/', views.Reggist_Ajax, name='jhcode'),#激活码验证
    path('logajax/',views.login_logic,name='logajax'),#异步登录验证
    path('searchajax/',views.SearchAjax),#异步搜索
    path('showmap/',views.Show_map,name='maps'), #数据可视化路径
    path('showpie/',views.PieChart,name="pie"),
    path('showhist/',views.Histogram,name='hist'),


]
