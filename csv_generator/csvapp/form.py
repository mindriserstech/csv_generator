from django import forms
from csvapp.models import CsvUser, CsvUserSchedule
from csvapp.models import CsvUserType
from django.db.models import fields

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = CsvUserType
        fields = "__all__"

class CsvUserRegisterForm(forms.ModelForm):
    class Meta:
        model = CsvUser
        fields = "__all__"

class CsvUserLoginForm(forms.ModelForm):
    class Meta:
        model = CsvUser
        fields = ('email', 'password',)

class CsvUserScheduleForm(forms.ModelForm):
    class Meta:
        model = CsvUserSchedule
        fields = "__all__"
