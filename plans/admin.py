
from django.contrib import admin

from .models import Plan, Plan_Category

# Register your models here.

class PlanAdmin(admin.ModelAdmin):

    model = Plan

    list_display = (
        'name',
        'plan_category',
        'plan_length',
        'days_per_week',
        'equipment_needed',
        'price',
        'image',
    )

    ordering = ('name',)

class Plan_CategoryAdmin(admin.ModelAdmin):
    model = Plan_Category

    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Plan, PlanAdmin)
admin.site.register(Plan_Category, Plan_CategoryAdmin)