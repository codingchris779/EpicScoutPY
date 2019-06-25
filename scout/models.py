from django.db import models
from jsonfield import JSONField


class Team(models.Model):
    TeamNum = models.CharField(max_length=200)
    TeamName = models.CharField(max_length=200)

    def __str__(self):
        return self.TeamNum


# Create your models here.
class Info(models.Model):
    Team = Team
    MatchNum = models.IntegerField
    isRed = models.fields.BooleanField

    def __str__(self):
        return "hi"


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    formInfo = Info

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
