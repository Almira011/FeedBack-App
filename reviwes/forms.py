from django import forms
from .models import Reviewtable

class review_form(forms.ModelForm):
    class Meta:
        model = Reviewtable
        fields = "__all__"