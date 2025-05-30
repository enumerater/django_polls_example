from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin


class Question(models.Model):
    def __str__(self):
        return self.question_text
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?",
        )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)