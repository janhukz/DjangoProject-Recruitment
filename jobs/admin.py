from django.contrib import admin
from jobs.models import Job


# Register your models here.

# 定义列表页展示哪些字段 , ModelAdmin是模型管理类
class JobAdmin(admin.ModelAdmin):
    # exclude 排除内容页不需要展示的字段
    exclude = ('creator', 'create_date', 'modified_date')
    # 列表页展示哪些字段
    list_display = ("job_name", "job_type", "job_responsibility", "creator", "create_date", "modified_date")

    # 当把这些字段隐藏后,直接提交,数据库里不会有这些属性,所以要用到 save_model 方法
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super(JobAdmin, self).save_model(request, obj, form, change)


# 注册模型到admin管理后台
admin.site.register(Job, JobAdmin)
