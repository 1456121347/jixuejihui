from organization.views import OrgView,AddUserAskView
from django.urls import path,re_path

app_name = "organization"

urlpatterns = [
# 机构页面路由
    path('list/',OrgView.as_view(),name='org_list'),
    path('add_ask/',AddUserAskView.as_view(),name="add_ask")
]