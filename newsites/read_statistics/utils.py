from django.contrib.contenttypes.models import ContentType
from .models import ReadNum

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get('blog_%s_readed' % obj):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # ���ڼ�¼
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)

        else:
            # �����ڶ�Ӧ��¼
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
    return key