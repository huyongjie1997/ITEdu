import xadmin
from .models import *

class CityInfoXadmin(object):
    '''城市信息'''
    list_display = ['name','add_time']
    model_icon = 'fa fa-hospital-o'


class OrgInfoXadmin(object):
    '''机构信息'''
    list_display = ['image', 'name','course_num','study_num','love_num','click_num','category','cityinfo']
    model_icon = 'fa fa-address-card-o'
    style_fields = {'detail':'ueditor'}


class TeacherInfoXadmin(object):
    '''讲师信息'''
    list_display = ['image', 'name','work_company', 'work_year', 'work_position', 'click_num', 'age', 'gender', 'love_num']
    model_icon = 'fa fa-user-circle'

xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherInfo,TeacherInfoXadmin)