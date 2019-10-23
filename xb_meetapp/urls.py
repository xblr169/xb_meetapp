"""xb_meetapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from app import  views,meviews,userViews
from app import meetViews as meet
from app import userViews as user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mee',meviews.meview.as_view()),
    path('user', userViews.userView.as_view()),
    url(r'^$',views.hello),
    url(r'^get-user/$',user.get_user),
    url(r'^depart/$',views.get_depart),
    url(r'^domain/$',views.get_domain),
    url(r'^room/$',views.get_room),
    url(r'^d-json/$',views.get_depart_byjson),
    url(r'^d-list/$',views.get_depart_bylist),
    url(r'^save-depart/$',views.save_depart),
    url(r'^login-depart/$', views.login_depart),
    url(r'^save-user/$',user.save_user),
    url(r'^login/$',user.login),
    url(r'^get-data/$',meet.get_data),
    url(r'^get-amy/$',meet.get_data_byamy),
    url(r'^get-abc/$',meet.get_data_byabc),
    url(r'^get-byuser/$', meet.get_data_byuser),
    url(r'^save-data/$',meet.save_data),
    #url(r'^mee/$',meviews.meview.as_view())
]
