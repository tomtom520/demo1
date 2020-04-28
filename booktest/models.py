from django.db import models

# Create your models here.


class AreaInfo(models.Model):

    atitle = models.CharField(max_length=20, verbose_name='地区') # verbos_name = 是指在后台显示名称
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='上级')

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle


# 返回父级地区名称
    def aprent(self):
        if self.aParent is None:
            return None
        return self.aParent.atitle

    title.admin_oder_field = 'id'  # p排序
    title.short_description = '地区名称' # 指定列标题
    aprent.short_description = '上级地区'  # 指定列标题
    aprent.admin_oder_field = 'atitle'  # p排序

    class Meta:
        db_table = 'areas'


class ImgTest(models.Model):
    """后台上传图片"""
    img_file = models.ImageField(upload_to='booktest', verbose_name='图片') # 指定图片放在midea下的路径

    class Meta:
        db_table = 'imgtest'