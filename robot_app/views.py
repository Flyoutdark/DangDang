import happybase
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_page
from redis import Redis
from authcode.image import ImageCaptcha
import os,random , hashlib,string
from django.http import HttpResponse, JsonResponse
import time
from spider.daily import daily_user ,Get_habse
from django.core.cache import cache
from robot_app.models import Creditpeople, Creditlost1, Users, Zhilian
from django.core.mail import send_mail, EmailMultiAlternatives
#注册部分
#1、信息的合法性验证邮箱注册及手机号注册
    #处理逻辑1、验证码与手机或邮箱的激活码的正确与否
            #2、输入的信息合法性，邮箱的合法性以及手机号的长度，是否都是数字
            #3、用户的重复性验证，是否已经注册过
            #4、用户密码加密处理
#2、手机注册与邮箱注册两种方式
    #1、切换注册方式时隐藏另外一个标签
#注册页面展示
def regist(request):

    return render(request,'register.html')

#异步验证用户名是否已存在
#1、从数据库中拿出数据，判断是否存在
def Reggist_Ajax(request):
    #获取用户的注册信息
    email=request.GET.get('email')
    usrtel = request.GET.get('usrtel')
    #从数据库中查询数据
    print(email,usrtel)
    emaildb=Users.objects.filter(email=email)
    usertel = Users.objects.filter(phone=usrtel)
    if email and emaildb:#判断是邮箱验证还是手机验证请求
        res = {"res": '1'}
        return JsonResponse(res)

    elif usertel and usrtel:#为真则手机已经注册
        res = {"res": '1'}
        return JsonResponse(res)
    else:
        res = {"res": '1'}
        return HttpResponse()
#生成随机激活码

def random_str():
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(6):
        s=random.choice(chars)
        str+=s
    print(str)
    return str
#验证激活码部分
#发送验证码给用户
def SendCode(request):
    useremail=request.GET.get('Email')
    codes = request.session['codes']=random_str()
    time1=time.time()
    request.session['time1']=time1#获取当前时间，存入session
    subject, from_email, to = '国务院的邀请函', 'flyandvi6@sina.com', useremail
    text_content = '欢迎访问!，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册!，您的激活码是:'+random_str()+'。\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p> '
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('ok')
    return JsonResponse({'ewe':34})




def regist_logic(request):
    code = request.POST.get('vcode')#用户输入的激活码
    codes = request.session.get('codes')
    time1=request.session.get('time1')
    time2 = time.time()
    time3=int(time2)-int(time1)#时间差
    if time3<60 and code==codes:
        try:
            userid = request.POST.get('userid')
            email = request.POST.get('email')
            pwd = request.POST.get('psw')
            usrtel = request.POST.get('usrtel')
            regtime=time.strftime( '%Y-%m-%d %X', time.localtime() )
            with transaction.atomic():

                Users(email=email,phone=usrtel,password=pwd,username=userid,regtime=regtime).save()
            # print(12312321312,userid,email,pwd,usrtel)
                return redirect('/robot/login/')
        except Exception:
            return redirect('/robot/regist/')
    else:
        return redirect('/robot/regist/')


def auth_code(request):
    image = ImageCaptcha(fonts=[os.path.abspath("authcode/simkai.ttf")])
    code_list = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    code = "".join(code_list)
    request.session["yzcode"]=code
    data = image.generate(code)
    return HttpResponse(data,"image/png")


#一、信息合法性验证，用户密码验证，验证码验证

def login(request):
    return render(request,'login.html')

#登录部分信息的异步验证
# def login_ajax(request):



#登录逻辑处理
def login_logic(request):
    user = request.POST.get('userid')#用户邮箱或手机
    pwd = request.POST.get('psw')#密码
    vcode = request.POST.get('vcode')#获取用输入的验证码
    yzcode=request.session.get("yzcode")#congsession中获取验证码
    print(user,pwd,vcode,yzcode)
    if user and pwd and vcode:
        try:
            print(6)
            if "@" in user:#用户邮箱验证
                print(7)
                if Users.objects.filter(email=user,password=pwd) and yzcode.lower==vcode.lower():
                    request.session['on']=user#用于登录住哪个台的判断
                    return JsonResponse({'filed':'ok'})
                else:
                    print(2)
                    return JsonResponse({'filed':"1"})

            else:
                print(8)
                if Users.objects.get(phone=user,password=pwd) and yzcode.lower()==vcode.lower():
                    request.session['on'] = user
                    return JsonResponse({'filed':'ok'})
                else:
                    print(3,yzcode.lower==vcode.lower())
                    return JsonResponse({'filed':"1"})
        except:
            print(5)
            return JsonResponse({'filed': "1"})
    else:
        print(4)
        return JsonResponse({'filed': "1"})



def main_page(request):
    return render(request,'main.html')



#搜索
def ConditionQuery(search_condition="北京",num=1):

    if type in ['北京', '上海', '深圳', '广州']:
        data = Paginator(object_list=Zhilian.objects.filter(city=search_condition), per_page=30).page(num)
        return data
    else:
        data = Paginator(object_list=Zhilian.objects.filter(zw__icontains=search_condition), per_page=30).page(num)
        return data


# 数据展示
def InformationBase(city='北京', type="AI"):
    data = Paginator(object_list=Zhilian.objects.filter(city=city,zw__icontains=type), per_page=30)#.page(num)
    return data

# def test(request):
#     search_condition = "北京"
#     num = int(request.GET.get("num"))
#     sdata = Paginator(object_list=Zhilian.objects.filter(city=search_condition), per_page=30).page(num)
#     res = render(request, 'menu.html', {'data': sdata})
#     request.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
#     return res

#某个城市下的某类类别展示及分页展示
#某类别下的所有数据
#页数小于10的时候从数据库那数据大于10从hbase拿
#日志记录用户名，所在城市，时间，访问的城市及职位信息
#redis 的缓存
#用户状态的记录，非登录状态仅查看十页
#条件查询



#左侧信息栏
@daily_user
# @cache_page(timeout=100,key_prefix="cacheRedis")
def menu_page(request):
    sp = request.COOKIES.get("spider")
    if sp:
        num=random.choice([1,2,3,4,5,6,7,8,9])
        sdata = ConditionQuery(num=num)
        res = render(request, 'menu.html', {'data': sdata})
        res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
        return res
    else:
        on = request.session.get('on')  # 用户状态
        num=int(request.GET.get("num"))#当前页页数
        type=request.GET.get("type")#左侧导航栏职业种类请求
        city=request.GET.get('city')#左侧导航栏城市请求
        if city:
            request.session['city'] = city#将条件存入session
            request.session['type'] = type
        city_session=request.session.get('city')#从session中取出参数
        type_session=request.session.get('type')
        # search_condition=request.GET.get("condition")#中间搜索栏城市或职位
        # request.session['search_condition']=search_condition
        # search_session=request.session.get('search_condition')
        # city_session=request.session.get('city')
        # type_session=request.session.get('type')
        #用户点击左侧菜单栏后进入此条件
        if city_session:
            idata = InformationBase(city=city_session, type=type_session)
                #此时页数超限，需从HBASE中获取数据，需要传递参数，用户进一步查看的何种信息
                #1、用户默认数据状态下一直翻页，无数据传回
                #2、用户点击左侧菜单栏信息后翻页
                #3.用户中间搜索页面翻页
            if num > 10 and on:
                condition=city_session+type_session
                data = Get_habse(condition).page(num)
                res=render(request, 'menu.html', {'data': data})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"),'latin-1'),max_age=0.3)
                return res
            # 2、小于10页情况
            elif num <= 10:
                data = idata.page(num)
                res=render(request, 'menu.html', {'data': data})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"),'latin-1'),max_age=0.3)
                return res
            else:  # 大于10页非登录状态，给与提示并把数据固定在第十页
                data = idata.page(10)
                off = '非登录状态仅显示10页！'
                res=render(request, 'menu.html', {'data': data})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"),'latin-1'),max_age=0.3)
                return res
        else:
            #首次进入只有页号参数且用户只翻页
            if num>10 and on :
                data = Get_habse('北京').page(num)
                res = render(request, 'menu.html', {'data': data})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
                return res
            # 2、小于10页情况
            elif num<=10:
                sdata=ConditionQuery(num=num)
                res=render(request, 'menu.html', {'data': sdata})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
                return res
            else :#大于10页非登录状态，给与提示并把数据固定在第十页
                sdata = ConditionQuery(num=10)
                off = '非登录状态仅显示10页！'
                res=render(request, 'menu.html', {'data': sdata})
                res.set_cookie("spider", str("杀虫剂".encode("utf-8"),'latin-1'),max_age=0.3)
                return res




# 搜索框搜索views
@daily_user
# @cache_page(timeout=100,key_prefix="cacheRedis")
def SearchAjax(request):
    sp = request.COOKIES.get("spider")
    if sp:
        time.sleep(15)
        return HttpResponse("页面加载失败！")
    else:
        num = int(request.GET.get("num"))
        on = request.session.get('on')  # 用户状态
        search_condition = request.GET.get("condition")  # 中间搜索栏城市或职位
        if search_condition:
            request.session['search_condition'] = search_condition  # 存入session下次翻页时取出
        search_session = request.session.get('search_condition')
        # 1、首次进入此views，num与 search_condition都存在
        # 2.2+次进入分页请求或更新条件查询
        # 3.不点击左侧菜单栏部分，search_session一直存在

        if num > 10 and on:
            # 此时页数超限，需从HBASE中获取数据，需要传递参数，用户进一步查看的何种信息
            sdata = Get_habse(search_session)  #
            data = sdata.page(num)
            res=render(request, 'menucopy.html', {'data': data})
            res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
            return res
        # 2、小于10页情况
        elif num <= 10:
            print(search_session,num)
            sdata = ConditionQuery(search_session, num=num)
            res = render(request, 'menucopy.html', {'data': sdata})
            res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
            return res
        else:  # 大于10页非登录状态，给与提示并把数据固定在第十页
            sdata = ConditionQuery(search_session, num=10)
            off = '非登录状态仅显示10页！'
            res = render(request, 'menucopy.html', {'data': sdata})
            res.set_cookie("spider", str("杀虫剂".encode("utf-8"), 'latin-1'), max_age=0.3)
            return res




    #方法二，views未分开处理，左侧与中间搜索栏共用一个views
  #   if city :
  # # 左侧数据展示数据对象
  #       request.session['city'] = city
  #       request.session['type'] = type
  #       if search_session:
  #           del request.session['search_condition']
  #       idata=InformationBase(city=city,type=type)
  #       if num > 10 and on:
  #           #此时页数超限，需从HBASE中获取数据，需要传递参数，用户进一步查看的何种信息
  #           #1、用户默认数据状态下一直翻页，无数据传回
  #           #2、用户点击左侧菜单栏信息后翻页
  #           #3.用户中间搜索页面翻页
  #           data = idata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       # 2、小于10页情况
  #       elif num <= 10:
  #           print(num, '页号')
  #           data = idata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       else:  # 大于10页非登录状态，给与提示并把数据固定在第十页
  #           data = idata.page(10)
  #           off = '非登录状态仅显示10页！'
  #           return render(request, 'menu.html', {'data': data, 'off': off})
  #   elif search_condition :
  #       if city_session:
  #           del request.session['city']
  #           del request.session['type']
  #       request.session['search_condition']=search_condition
  #       sdata=ConditionQuery(search_condition)
  #       if num>10 and on :
  #           data =sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       # 2、小于10页情况
  #       elif num<=10:
  #           sdata = ConditionQuery(search_condition)  # 条件查询数据对象
  #           data = sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #           data = sdata.page(10)
  #           off = '非登录状态仅显示10页！'
  #           return render(request, 'menu.html', {'data': data, 'off': off})
  #   elif city_session:
  #       idata=InformationBase(city=city_session,type=type_session)
  #       if num > 10 and on:
  #           data = idata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       # 2、小于10页情况
  #       elif num <= 10:
  #           print(num, '页号')
  #           data = idata.page(num)
  #           print(data)
  #           return render(request, 'menu.html', {'data': data})
  #       else:  # 大于10页非登录状态，给与提示并把数据固定在第十页
  #           data = idata.page(10)
  #           off = '非登录状态仅显示10页！'
  #           return render(request, 'menu.html', {'data': data, 'off': off})
  #
  #   elif search_session:
  #       sdata=ConditionQuery(search_session)
  #       if num>10 and on :
  #           data =sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       # 2、小于10页情况
  #       elif num<=10:
  #           sdata = ConditionQuery(search_condition)  # 条件查询数据对象
  #           data = sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #           data = sdata.page(10)
  #           off = '非登录状态仅显示10页！'
  #           return render(request, 'menu.html', {'data': data, 'off': off})
  #   else:
  #       sdata=ConditionQuery()
  #       if num>10 and on :
  #           data =sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       # 2、小于10页情况
  #       elif num<=10:
  #           sdata = ConditionQuery()  # 条件查询数据对象
  #           data = sdata.page(num)
  #           return render(request, 'menu.html', {'data': data})
  #       else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #           data = sdata.page(10)
  #           off = '非登录状态仅显示10页！'
  #           return render(request, 'menu.html', {'data': data, 'off': off})
#方法二结束

#views分析及测试代码
  #   #1、页数小于等于10时，不从hbase取数据，不分用户状态，则先判断页数是否大于10页
  #   #用户状态，登录与非登录，请求大于10或小于10，可分为三类。
  #   # 1、登录状态下大于10页的请求，
  #   # 2、小于10页的请求，不区分登录状态，
  #   # 3、非登陆状态下大于10页的请求
  #   # if num is not None:
  #   # 1、页号大于10且为登录状态
  #
  #
  #   # print(idata.page(num))
  #   #点击条件查询那功能按钮执行此代码
  #   # if search_condition :
  #   #     request.session['search']='1'
  #   #     if num>10 and on :
  #   #         data =sdata.page(num)
  #   #         return render(request, 'menu.html', {'data': data})
  #   #     # 2、小于10页情况
  #   #     elif num<=10:
  #   #             data = sdata.page(num)
  #   #             return render(request, 'menu.html', {'data': data})
  #   #     else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #   #         data = sdata.page(10)
  #   #         off = '非登录状态仅显示10页！'
  #   #         return render(request, 'menu.html', {'data': data, 'off': off})
  #   #点击左侧功能部分执行以下代码
  #   # if flag:
  #   #     request.session['city'] = city
  #   #     request.session['city'] = type
  #   #     if num>10 and on :
  #   #         data =flag.page(num)
  #   #         return render(request, 'menu.html', {'data': data})
  #   #     # 2、小于10页情况
  #   #     elif num<=10:
  #   #         print(num,'页号')
  #   #         data =flag.page(num)
  #   #         return render(request, 'menu.html', {'data': data})
  #   #     else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #   #         data = flag.page(10)
  #   #         off = '非登录状态仅显示10页！'
  #   #         return render(request, 'menu.html', {'data': data, 'off': off})
  #   # #进入主页后直接点击下一页执行以下代码
  #   # else:
  #   #     print(1)
  #   #     # del session["base"]
  #   #     if num>10 and on :
  #   #         data =sdata.page(num)
  #   #         return render(request, 'menu.html', {'data': data})
  #   #     # 2、小于10页情况
  #   #     elif num<=10:
  #   #         sdata = ConditionQuery(search_condition)  # 条件查询数据对象
  #   #         data = sdata.page(num)
  #   #         return render(request, 'menu.html', {'data': data})
  #   #     else :#大于10页非登录状态，给与提示并把数据固定在第十页
  #   #         data = sdata.page(10)
  #   #         off = '非登录状态仅显示10页！'
  #   #         return render(request, 'menu.html', {'data': data, 'off': off})


def introduce(request):
    return render(request,'introduce.html')




#数据可视话展示
#地图
def Show_map(request):
    Get_habse()
    pass

#饼图
def PieChart(request):
    print(222)
    python = Get_habse('python').count
    ai = Get_habse("AI").count
    spider = Get_habse("爬虫").count
    bigdb = Get_habse("大数据").count
    return render(request,'饼图.html',{'python': python, 'ai': ai, 'spider': spider, 'bigdb':bigdb})
#柱状图
def Histogram(request):
    print(111)
    bj = int(Get_habse('北京').count)
    sh = Get_habse("上海").count
    gz = Get_habse("广州").count
    sz = Get_habse("深圳").count
    print(bj,sh,gz,sz)

    return render(request,'柱状图.html',{'bj': bj, 'sh': sh, 'gz': gz, 'sz': sz})

