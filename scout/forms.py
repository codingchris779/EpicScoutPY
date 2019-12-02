from django import forms
from .models import Team, Info


class InfoForm(forms.Form):
    side = forms.ChoiceField(choices=[(True, 'Red'), (False, 'Blue')])
    team = forms.ChoiceField(choices=[(t.id, t) for t in Team.objects.order_by('TeamNum')[:30]])
    round = forms.IntegerField(min_value=1, max_value=150)

class SkystoneForm(forms.Form):
    matchNum = forms.IntegerField()
    position = forms.ChoiceField()
    teamNum = forms.IntegerField()
    # teamName = forms.CharField() # make autofillable from above

    AUTO_StonesAcross = forms.IntegerField(max_value=6)
    AUTO_StonesPlaced = forms.IntegerField(max_value=AUTO_StonesAcross)
    AUTO_FirstSkystones = forms.IntegerField(max_value=2)
    AUTO_Parking = forms.BooleanField()

    DRIVER_StonesAcross = forms.IntegerField()
    DRIVER_StonesPlaced = forms.IntegerField() # automatically include Auto placements
    DRIVER_TallestStack = forms.IntegerField() # max_value=DRIVER_StonesPlaced

    END_MarkerHeight = forms.IntegerField()
    END_Parking = forms.BooleanField()
    
    POST_Comments = forms.Textarea()
    POST_Breakage = forms.BooleanField()


class MatchForm(forms.Form):
    Did_They_Run = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    Landing = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    Sampling = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    Claiming = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    Park = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    Gold_In_Cargo = forms.IntegerField()
    Silver_In_Cargo = forms.IntegerField()
    Depot = forms.IntegerField()
    How_Many_Seconds_Were_They_Broke = forms.IntegerField()
    Endgame = forms.ChoiceField(choices=[('H', 'Hang'), ('pp', 'Partial Park'), ('fp', 'Full Park')])
    Penalties = forms.IntegerField()
    Comments = forms.CharField()
