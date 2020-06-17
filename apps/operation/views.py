from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
class TeachersListView(View):
    def get(self,request):
        return render(request,'operation/teachers-list.html')