from django import forms

class PointWise(forms.Form):
    score = forms.FloatField()

class PairWise(forms.Form):
    score = forms.IntegerField()

class ListWise(forms.Form):
    score = forms.IntegerField()

