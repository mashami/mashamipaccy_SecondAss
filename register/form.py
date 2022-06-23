from django import forms
from .models import *

class TraineesForms(forms.ModelForm):
    # names=forms.CharField(required=True)
    # email=forms.CharField(required=True)
    # userName=forms.CharField(required=True)
    # dob=forms.CharField(required=True)
    # location=forms.CharField(required=True)

    
    class Meta:
        model = Tranees
        fields = "__all__"