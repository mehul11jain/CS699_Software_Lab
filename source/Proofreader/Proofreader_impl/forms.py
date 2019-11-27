from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your text here...','id':'q'}),label="")