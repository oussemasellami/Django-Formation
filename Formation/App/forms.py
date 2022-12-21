from django import forms
from django.forms import Textarea

from App.models import projet


class AjoutForm(forms.ModelForm):

    class Meta:
        model = projet
        fields = ("nom_projet", "duree_projet",
                  "createur", "temps_alloue", "suprviseur")
        widgets = {'nom_projet': Textarea(attrs={'cols': 10, 'rows': 4})}
