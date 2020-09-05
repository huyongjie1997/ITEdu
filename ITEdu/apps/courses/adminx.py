import xadmin
from .models import *

# Create your models here.
class CourseInfoXadmin(object):
    """课程信息"""
    list_display = ['image','name','study_num','level','love_num','category','orginfo','teacherinfo']
    model_icon = 'fa fa-book'
    style_fields = {'detail':'ueditor'}
class LessonInfoXadmin(object):
    """章节信息"""
    list_display = ['name', 'courseinfo', 'add_time']
    model_icon = 'fa fa-tags'

class VideoInfoXadmin(object):
    '''视频信息'''
    list_display = ['name', 'study_time', 'url','lessoninfo']
    model_icon = 'fa fa-play-circle'

class SourceInfoXadmin(object):
    """资源信息"""
    list_display = ['name', 'down_load', 'courseinfo', 'add_time']
    model_icon = 'fa fa-file-text'
xadmin.site.register(CourseInfo,CourseInfoXadmin)
xadmin.site.register(LessonInfo,LessonInfoXadmin)
xadmin.site.register(VideoInfo,VideoInfoXadmin)
xadmin.site.register(SourceInfo,SourceInfoXadmin)