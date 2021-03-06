"""GuLiEdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
import xadmin
from users.views import index
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^users/',include(('users.urls', "users"),namespace='users')),
    url(r'^courses/', include(('courses.urls',"courses" ),namespace='courses')),
    url(r'^orgs/', include(('orgs.urls',"orgs"), namespace='orgs')),
    url(r'^operations/', include(('operations.urls',"operations" ),namespace='operations')),
    url(r'^$',index,name='index')
]

handler404 = 'users.views.handler_404'
handler500 = 'users.views.handler_500'
