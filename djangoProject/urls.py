"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from o2o import views,viewsinfo,viewsdetail,viewsorders,viewswastes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o2o/', include('o2o.urls')),
    path('',views.index,name='index'),

    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('register',views.register,name='register'),

 # 后台用户管理
#管理员
    path('users', viewsinfo.usersindex, name="myadmin_usersindex"),
    path('usersadd', viewsinfo.usersadd, name="myadmin_usersadd"),
    path('usersinsert', viewsinfo.usersinsert, name="myadmin_usersinsert"),
    re_path(r'^usersdel/(?P<uid>[0-9]+)$', viewsinfo.usersdel, name="myadmin_usersdel"),
    re_path(r'^usersedit/(?P<uid>[0-9]+)$', viewsinfo.usersedit, name="myadmin_usersedit"),
    re_path(r'^usersupdate/(?P<uid>[0-9]+)$', viewsinfo.usersupdate, name="myadmin_usersupdate"),
#用户
    path('yonghu', viewsinfo.yonghuindex, name="myadmin_yonghuindex"),
    re_path(r'^yonghuedit/(?P<uid>[0-9]+)$', viewsinfo.yonghuedit, name="myadmin_yonghuedit"),
    re_path(r'^yonghuupdate/(?P<uid>[0-9]+)$', viewsinfo.yonghuupdate, name="myadmin_yonghuupdate"),

#回收员
    path('huishouyuan', viewsinfo.huishouyuanindex, name="myadmin_huishouyuanindex"),
    re_path(r'^huishouyuanedit/(?P<uid>[0-9]+)$', viewsinfo.huishouyuanedit, name="myadmin_huishouyuanedit"),
    re_path(r'^huishouyuanupdate/(?P<uid>[0-9]+)$', viewsinfo.huishouyuanupdate, name="myadmin_huishouyuanupdate"),



# 后台废品类别信息管理
    path('type', viewswastes.typeindex, name="myadmin_typeindex"),
    re_path(r'^typeadd/(?P<tid>[0-9]+)$', viewswastes.typeadd, name="myadmin_typeadd"),
    path('typeinsert', viewswastes.typeinsert, name="myadmin_typeinsert"),
    re_path(r'^typedel/(?P<tid>[0-9]+)$', viewswastes.typedel, name="myadmin_typedel"),
    re_path(r'^typeedit/(?P<tid>[0-9]+)$', viewswastes.typeedit, name="myadmin_typeedit"),
    re_path(r'^typeupdate/(?P<tid>[0-9]+)$', viewswastes.typeupdate, name="myadmin_typeupdate"),

    # 后台废品信息管理
    path('goods', viewswastes.goodsindex, name="myadmin_goodsindex"),
    re_path(r'^goodsadd/(?P<gid>[0-9]+)$', viewswastes.goodsadd, name="myadmin_goodsadd"),
    path('goodsinsert', viewswastes.goodsinsert, name="myadmin_goodsinsert"),
    re_path(r'^goodsdel/(?P<gid>[0-9]+)$', viewswastes.goodsdel, name="myadmin_goodsdel"),
    re_path(r'^goodsedit/(?P<gid>[0-9]+)$', viewswastes.goodsedit, name="myadmin_goodsedit"),
    re_path(r'^goodsupdate/(?P<gid>[0-9]+)$', viewswastes.goodsupdate, name="myadmin_goodsupdate"),

    #后台订单列表
    path('orders', viewsorders.ordersindex, name="myadmin_ordersindex"),
    path('addborders', viewsorders.addordersindex, name="myadmin_addordersindex"),
    path('orderssinsert', viewsorders.ordersinsert, name="myadmin_ordersinsert"),
    path('ordershisordes', viewsorders.ordershisordes, name="myadmin_ordershisordes"),
    re_path(r'ordersdel/(?P<uid>[0-9]+)$', viewsorders.ordersdel, name="myadmin_ordersdel"),
    re_path(r'ordersfabu/(?P<uid>[0-9]+)$', viewsorders.ordersfabu, name="myadmin_ordersfabu"),
    re_path(r'^ordersedit/(?P<uid>[0-9]+)$', viewsorders.ordersedit, name="myadmin_ordersedit"),
    re_path(r'^ordersupdate/(?P<uid>[0-9]+)$', viewsorders.ordersupdate, name="myadmin_ordersupdate"),

    #回收员操作
    path('orders_center', viewsdetail.hsyordersindex, name="myadmin_hsy_ordersindex"),
    path('finish_ordersindex', viewsdetail.finish_ordersindex, name="myadmin_finish_ordersindex"),
    path('yijie_ordersindex', viewsdetail.yijie_ordersindex, name="myadmin_yijie_ordersindex"),
    re_path(r'^orderswancheng/(?P<uid>[0-9]+)$',viewsdetail.orderswancheng,name="myadmin_orderswancheng"),
    re_path(r'^ordersjiedan/(?P<uid>[0-9]+)$',viewsdetail.ordersjiedan,name="myadmin_ordersjiedan"),
    #后台订单详情
    re_path(r'^detail/(?P<uid>[0-9]+)$',viewsdetail.detailindex,name="myadmin_detailindex"),
    #概况，资源统计
    path('count',views.count,name='myadmin_count'),
]