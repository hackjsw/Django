from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        #显示字段内容
        return self.type_name

class Blog(models.Model):
    #定义显示内容名称
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>"%self.title

