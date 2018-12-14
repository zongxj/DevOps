from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'votes', 'question']

admin.site.register(Choice, ChoiceAdmin)