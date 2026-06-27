from django.contrib import admin
from .models import Status, CashType, Category, Subcategory, CashFlow

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CashType)
class CashTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cash_type')
    list_filter = ('cash_type',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category__cash_type', 'category')

@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'cash_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('status', 'cash_type', 'category')
    date_hierarchy = 'date'

