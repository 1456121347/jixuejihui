from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from .models import CourseOrg,CityDict

'''
    课堂机构
'''

# class OrgView(View):
#
#     def get(self,request):
#         all_orgs = CourseOrg.objects.all()
#         org_onums = all_orgs.count()
#         all_citys = CityDict.objects.all()
#         try:
#             page = request.GET.get('page',1)
#         except PageNotAnInteger:
#             # 如果用户请求的页码号不是整数，显示第一页
#             page = 1
#         p = Paginator(all_orgs,2,request=request)
#         page_orgs = p.page(page)
#
#         context = {
#             "all_orgs": page_orgs,
#             "org_onums": org_onums,
#             "all_citys": all_citys,
#         }
#         return render(request,'organization/org-list.html',context)


class OrgView(View):
    '''
    课程机构
    '''
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            # 如果用户请求的页码号不是整数，显示第一页
            page_orgs = 1
        p = Paginator(all_orgs,3,request=request)
        page_orgs = p.page(page)

        org_onums = all_orgs.count()
        all_citys = CityDict.objects.all()
        context = {
            "all_orgs": page_orgs,
            "org_onums": org_onums,
            "all_citys": all_citys,
        }
        return render(request,'organization/org-list.html',context)