import xadmin
from .models import BannerInfo,EmailVerifyCode
from xadmin import views
#配置xadmin主题,注册的时候要用到专用的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True

class CommXadminSetting(object):
    site_title = 'IT教育后台管理系统'
    site_footer = 'IT教育'
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    '''轮播图信息'''
    list_display = ['image','url','add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']
    model_icon = 'fa fa-picture-o'

class EmailVerifyCodeXadmin(object):
    '''邮箱验证码信息'''
    list_display = ['code', 'email', 'send_type','add_time']
    model_icon = 'fa fa-envelope-o'


xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
#注册主题类
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)
#注册全局样式的类
xadmin.site.register(views.CommAdminView,CommXadminSetting)