from django.urls import path,re_path

from .views import TeachersListView

app_name = "operation"
urlpatterns = [
    path('list/',TeachersListView.as_view(),name="teachers_list"),
# 讲师列表
    re_path('teacher/list/', TeachersListView.as_view(), name="teacher_list"),
]