from django.shortcuts import render_to_response, get_object_or_404,render
from .models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def blog_list_common_data(request,blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_OF_BLOGS)  # 每10篇进行分页
    page_num = request.GET.get('page', 1)  # 获取页码参数(GET请求)
    page_of_blogs = paginator.get_page(page_num)
    # currentr_page_num = page_of_blogs.number #获取当前页码
    page_range = [x for x in range(int(page_num) - 2, int(page_num) + 3) if 0 < x <= paginator.num_pages]
    # page_of_blogs.object_list = panginator.get_page()
    # 加省略页码标记
    if page_range[0] - 1 > 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] > 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {
        'blogs': page_of_blogs.object_list,
        'page_of_blogs': page_of_blogs,
        'blog_types': BlogType.objects.all(),
        'page_range': page_range,
        'blogs_all_list': blogs_all_list,
        'blog_dates': Blog.objects.dates('created_time', 'month', order='DESC'),
    }

    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = blog_list_common_data(request,blogs_all_list)
    # 另外一个统计数量的方法
    # context['blogs_count'] = Blog.objects.all().count()
    return render(request,'blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    context = {
        'previous_blog': Blog.objects.filter(created_time__gt=blog.created_time).last(),
        'next_blog': Blog.objects.filter(created_time__lt=blog.created_time).first(),
        'blog': blog,

    }
    return render(request,'blog/blog_detail.html', context)

def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = blog_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type
    return render(request,'blog/blogs_with_type.html', context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = blog_list_common_data(request,blogs_all_list)
    context['blogs_with_date'] = "{0}年{1}月".format(year, month)
    return render(request,'blog/blogs_with_date.html', context)
