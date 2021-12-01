from django.contrib import admin
from .models import Plan, Image

class PlanImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanImageInline]
    
admin.site.register(Plan, PlanAdmin)
# Register your models here.
