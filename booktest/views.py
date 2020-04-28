from django.shortcuts import render, HttpResponse
from django.conf import settings
from booktest.models import ImgTest, AreaInfo
from demo1.settings import MEDIA_ROOT
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.


def static_test(request):
    return render(request, 'booktest/static_test.html')


# /index
def index(request):
    # 获取访问d的ip地址
    addr = request.META['REMOTE_ADDR']
    return render(request, 'booktest/index.html', {'addr': addr})


# /upload_handle
def upload_handle(request):
    # 1、获取文件对象 ,文件在请求中以字典形式存在
    file_ob = request.FILES['pic']
    # 2、创建文件
    file_path = "%s/booktest/%s" %(MEDIA_ROOT, file_ob.name)
    print(file_ob.name)
    # 3、将内容写入创建的文件中
    with open(file_path, 'wb') as f:
        for content in file_ob.chunks():
            f.write(content)
    # 4、像数据库中插入记录
    ImgTest.objects.create(img_file='booktest/%s' %file_ob.name)
    # 5、返回响应
    return HttpResponse("ok")


# /upload
def upload(request):
    return render(request, 'booktest/upload.html')


#/show_area页码    分页显示
def show_area(request, pindex):
    # 1,get objects contents
    areas = AreaInfo.objects.filter(aParent__isnull=True).order_by('atitle')
    # 2, let the contents splite apge
    paginator = Paginator(areas, 10)
    # 3, get every page content
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.get_page(pindex)
    # 4, renturn html and content
    return render(request, 'booktest/show_area.html', {'page': page})


# /areas
def areas(request):
    """返回获取地区信息首页"""
    return render(request, "booktest/areas.html")


# /prov
def prov(request):
   """返回省级信息函数"""
   areas = AreaInfo.objects.filter(aParent__isnull=True)
   area_list = []
   for ar in areas:
       area_list.append((ar.id, ar.atitle))
   return JsonResponse({'data':area_list})


# /city
def city(request, num):
    """返回市级信息函数和县级信息函数"""
    areas = AreaInfo.objects.filter(aParent__id=num)
    area_list = []
    for ar in areas:
        area_list.append((ar.id, ar.atitle))
    return JsonResponse({'data': area_list})

