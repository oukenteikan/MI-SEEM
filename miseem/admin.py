from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'standard')
    ordering = ('description',)

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('belong_to_system', 'belong_to_question', 'content')
    ordering = ('content', )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('belong_to_question', 'belong_to_noter', 'type', 'time')
