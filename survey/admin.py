from django.contrib import admin

# Register your models here.
from .models import Servey,Question, Option , OpenOption , ShortOption

class ServeyQuestionInline(admin.TabularInline):
    model = Question
    
class ServeyAdmin(admin.ModelAdmin):
    inlines = [ServeyQuestionInline]
    
class QuestionNormalOptionInline(admin.TabularInline):
    model = ShortOption
    
class QuestionOpenOptionInline(admin.TabularInline):
    model = OpenOption
    
class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [QuestionNormalOptionInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Servey,ServeyAdmin)