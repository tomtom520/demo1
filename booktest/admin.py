from django.contrib import admin
from booktest.models import AreaInfo, ImgTest
# Register your models here.


# 块级返回子级地区
class AreaInfoStack(admin.StackedInline):
    # 这里写一对多中的多的模型类类名
    model = AreaInfo
    extra = 5 # 额外增加的空白添加框
    # 无法控制返回值

    # def __str__(self):
    #     return self.model.id


class AreaInfoTabular(admin.TabularInline):
    # 这里写一对多中的多的模型类类名
    model = AreaInfo
    # 额外增加的空白添加框
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 # z指定每一页显示数据
    list_display = ['id', 'title', 'aprent'] # 可以写model的属性，也可以写他的方法
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['id'] # 列表页右侧过滤栏
    search_fields = ['id', 'atitle']  # 列表页搜索框
    #fields = ['atitle', 'id']
    fieldsets = (
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']})
    )

    inlines = [AreaInfoTabular]


# model注册一下，这样才能显示
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(ImgTest)