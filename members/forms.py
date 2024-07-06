from django import forms
from .models import submission

class submissionForm(forms.ModelForm):
    class Meta:
        model = submission
        fields = ['name','email','phone_number']