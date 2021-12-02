from django.contrib import admin

# Register your models here.
from .models import Survey,Question, Option 

class ServeyQuestionInline(admin.TabularInline):
    model = Question
    
class ServeyAdmin(admin.ModelAdmin):
    inlines = [ServeyQuestionInline]
    

class OptionInline(admin.TabularInline):
    model = Option
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Survey,ServeyAdmin)