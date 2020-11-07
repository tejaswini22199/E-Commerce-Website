from django import forms
from .models import sellproduct


class sell(forms.ModelForm):
    class Meta:
        model=sellproduct
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'product':forms.TextInput(attrs={'class':'form-control'}),
            'cost':forms.TextInput(attrs={'class':'form-control'}),
           
        }