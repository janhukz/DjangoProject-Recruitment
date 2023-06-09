from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# 定义JobTypes,元组列表
JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
]
Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    # 使用ForeignKey表示引用另一个模型, 删除数据的时候,外键关联处理的逻辑 on_delete 的行为
    creator = models.ForeignKey(User, verbose_name="创建人", on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改时间", default=datetime.now)
