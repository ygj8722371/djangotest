from django.db import models
from project_app.models import Project

# Create your models here.

class Module(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=50,null=False)
    describe = models.TextField("描述",default='')
    create_time = models.DateTimeField("日期",auto_now_add=True)

    def __str__(self):
        return self.name