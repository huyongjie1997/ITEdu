# operation/adminx.py

import xadmin

from .models import UserAsk, UserLove, UserCourse, UserComment, UserMessage


class UserAskAdmin(object):
    '''咨询信息'''

    list_display = ['name', 'phone', 'course', 'add_time']
    search_fields = ['name', 'phone', 'course']
    list_filter = ['name', 'phone', 'course', 'add_time']
    model_icon = 'fa fa-phone-square'

#
class UserCourseAdmin(object):
    '''用户学习课程信息'''

    list_display = ['study_man', 'study_course', 'add_time']
    search_fields = ['study_man', 'study_course']
    list_filter = ['study_man', 'study_course', 'add_time']
    model_icon = 'fa fa-pencil-square-o'




class UserMessageAdmin(object):
    '''用户消息信息'''

    list_display = ['message_man', 'message_content', 'message_status', 'add_time']
    search_fields = ['message_man', 'message_content', 'message_status']
    list_filter = ['message_man', 'message_content', 'message_status', 'add_time']
    model_icon = 'fa fa-volume-up'


class UserCommentAdmin(object):
    '''用户评论课程信息'''

    list_display = ['comment_man', 'comment_course', 'comment_content', 'add_time']
    search_fields = ['comment_man', 'comment_course', 'comment_content']
    list_filter = ['comment_man', 'comment_course', 'comment_content', 'add_time']
    model_icon = 'fa fa-commenting-o'



class UserLoveAdmin(object):
    '''用户收藏后台'''

    list_display = ['love_man', 'love_id', 'love_type', 'add_time']
    search_fields = ['love_man', 'love_id', 'love_type']
    list_filter = ['love_man', 'love_id', 'love_type', 'add_time']
    model_icon = 'fa fa-chain-broken'


# 将后台管理器与models进行关联注册。
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserComment, UserCommentAdmin)
xadmin.site.register(UserLove, UserLoveAdmin)