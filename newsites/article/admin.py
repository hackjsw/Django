from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)#注册到admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content','author', 'is_deleted','created_time', 'last_updated_time')#显示内容
    ordering = ('id',)#排列顺序
    pass

#admin.site.register(Article,ArticleAdmin)#注册到admin