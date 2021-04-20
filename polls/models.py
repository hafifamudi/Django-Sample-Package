import datetime


from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #custome the pub_date property and header in admin user interface
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    # costume method
    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date < now


    def __str__(self):
        return f'Question Text : {self.question_text} and Publish Date {self.pub_date}'
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return f'Choice Text : {self.choice_text} and Votes {self.votes}'
    
