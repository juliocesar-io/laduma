from django import forms
from .models import Package, Template, Order

class Step1Form(forms.ModelForm):
    template = forms.ModelChoiceField(queryset=Template.objects.all(), label='')
    packages = forms.ModelMultipleChoiceField(queryset=Package.objects.all(),  widget=forms.CheckboxSelectMultiple(), label='')

    class Meta:
        model = Order
        fields = ['template', 'packages']



class Step2Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'},))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'type': 'email'},))