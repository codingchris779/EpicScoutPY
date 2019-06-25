from django import forms
from .models import Team


class InfoForm(forms.Form):
    side = forms.ChoiceField(choices=[(True, 'Red'), (False, 'Blue')])
    team = forms.ChoiceField(choices=[(t.id, t) for t in Team.objects.order_by('TeamNum')[:30]])
    round = forms.IntegerField(min_value=1, max_value=150)

