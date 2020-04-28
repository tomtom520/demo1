from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# 定义IP地址过滤类
class CheckIPSMiddleware(MiddlewareMixin):
    IPS = ['127.0.1.1']

    # 定义处理函数
    def process_view(self, request, view_func, *args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in CheckIPSMiddleware.IPS:
            return HttpResponse('<h1>Forbidden Visit</h1>')



# class TestMiddleware(MiddlewareMixin):
#
#     # __init__
#     def  __ini__(self):
#         print("-----init----服务器重启后接收到第一个请求")
#
#     def process_request(self, request):
#         print('----process_request------url匹配之前')
#
#     def process_view(self, request, view_func, *args, **kwargs):
#         print('---process_view_____view执行之前')
#
#     def process_response(self, request, response):
#         print('_____process_response____')
#         return response