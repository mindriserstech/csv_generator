from django import forms
from csvapp.models import CsvUserType
from django.db.models import fields

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = CsvUserType
        fields = "__all__"
