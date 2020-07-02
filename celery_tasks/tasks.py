# 使用celery
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
import time

# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
# django.setup()

from goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner, GoodsSKU
from django_redis import get_redis_connection
# 创建一个Celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://192.168.116.134:6379/8')

# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    # 組織邮件信息
    # 發送激活信息
    subject = '天天生鲜欢迎信息'
    massage = '郵件正文'
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_massage = '<h1>%$, 欢迎您成为天天生鲜会员，</h1>请点击下面链接激活用户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>'%(username, token, token)

    send_mail(subject, massage, sender, receiver, html_massage=html_massage)
    time.sleep(5)


def genrate_static_index_html():
    '''生成首頁靜態頁面'''
    """
          显示首页，如果访问的是/index的话直接调用视图函数去重新查询一遍
              如果直接访问域名的话，那么加载的是celery服务器中已经渲染好的html代码，不需要数据库重新 查询
              当管理员更新后台的时候，会自动celery重新生成静态html网页，不影响使用
          """
    # 尝试从缓存中获取数据
    context = cache.get('index_page_data')
    if context is None:
        # 获取商品的种类信息
        types = GoodsType.objects.all()

        # 获取轮播图信息
        banners = IndexGoodsBanner.objects.all().order_by('index')

        # 获取促销信息
        promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

        # 获取首页分类商品展示信息
        for type in types:
            image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
            title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')

            type.image_banners = image_banners
            type.title_banners = title_banners

        # 上面查询出来的结果都一样，设置缓存
        context = {
            'types': types,
            'goods_banners': banners,
            'promotion_banners': promotion_banners,
        }
        cache.set('index_page_data', context, 3600)

    # 获取首页购物车的数目
    if request.user.is_authenticated:
        conn = get_redis_connection('default')
        cart_key = 'cart_%s' % request.user.id
        cart_count = conn.hlen(cart_key)
    else:
        cart_count = 0

    context.update(cart_count=cart_count)

    return render(request, 'index.html', context=context)