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
        return "hi"


class TeamMatch(models.Model):
    info = models.OneToOneField(Info, on_delete=models.CASCADE, primary_key=False, default='')
    Did_They_Run = models.BooleanField(default=False)
    Landing = models.BooleanField(default=False)
    Sampling = models.BooleanField(default=False)
    Claiming = models.BooleanField(default=False)
    Park = models.BooleanField(default=False)
    Gold_In_Cargo = models.IntegerField(default='0')
    Silver_In_Cargo = models.IntegerField(default='0')
    Depot = models.IntegerField(default='0')
    How_Many_Seconds_Were_They_Broke = models.IntegerField(default='0')
    Endgame = models.CharField(max_length=5, default='3')
    Penalties = models.IntegerField(default='0')
    Comments = models.CharField(max_length=500, default='lols')


class Match(models.Model):
    MatchNum = models.IntegerField
    rd = TeamMatch()
    rc = TeamMatch()
    bd = TeamMatch()
    bc = TeamMatch()

