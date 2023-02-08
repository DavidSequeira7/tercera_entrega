from django import forms

class MovieForm(forms.Form):
    name = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=50)
    year = forms.IntegerField(min_value=1900, max_value=2022)
    origin = forms.CharField(max_length=50)
    duration = forms.IntegerField()
    director = forms.CharField(max_length=100)
    cast = forms.CharField(widget=forms.Textarea)
    rating = forms.FloatField()