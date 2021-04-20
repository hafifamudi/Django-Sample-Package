from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #custome the the header of Question Model
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #filter using pub_date field
    list_filter = ['pub_date']
    
    #search base on question_text field 
    search_fields = ['question_text']

    #custome label name of Question Model
    fieldsets =  [
        (None,              {'fields': ['question_text']},),
        ('Date Information', {'fields': ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
