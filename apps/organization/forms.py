from django import forms

# class UserAskForm(forms.Form):
#     name = forms.CharField()
#     mobile = forms.CharField()
#     course_name = forms.CharField()

from django import forms

from apps.operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

