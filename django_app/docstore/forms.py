from django import forms
from .models import app_name


class BookForm(forms.ModelForm):
    class Meta:
        model = app_name
        fields = ('app','btitle','pdf','author','doc_type')