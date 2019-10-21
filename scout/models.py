from django.db import models
from jsonfield import JSONField


class Team(models.Model):
    TeamNum = models.CharField(max_length=200)
    TeamName = models.CharField(max_length=200)
    matches = []

    def __str__(self):
        return self.TeamNum


# Create your models here.
class Info(models.Model):
    Team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=False, null=False)
    MatchNum = models.IntegerField
    isRed = models.fields.BooleanField

    def __str__(self):
        return "Hi!"


class SkystoneMatch(models.Model):
    info = models.OneToOneField(Info, on_delete=models.CASCADE, primary_key=False, default='')
    Did_They_Run = models.BooleanField(default=False)

    AUTO_Stones_Across = models.IntegerField(default='0')
    AUTO_SS_Across = models.IntegerField(default='0')
    AUTO_Parking = models.BooleanField(default=False)
    Stones_Across = models.IntegerField(default='0', help_text="Enter total (including auto) number of stones moved.")
    Stones_Placed = models.IntegerField(default='0')
    Tallest_Stack = models.IntegerField(default='0')
    END_TM_Height = models.IntegerField(default='0')
    END_Parking = models.BooleanField(default=False)
    Broken_Time = models.IntegerField(default='0', null=True, blank=True)
    Comments = models.CharField(max_length=500, default='n/a')


class Match(models.Model):
    MatchNum = models.IntegerField
    rf = SkystoneMatch()  # redFront
    rb = SkystoneMatch()  # redBack
    bf = SkystoneMatch()  # blueFront
    bb = SkystoneMatch()  # blueBack
