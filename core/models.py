from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Статус")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Статус"
        verbose_name_plural="Статусы"

class CashType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тип")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"
    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Катеория")
    cash_type = models.ForeignKey(CashType, on_delete=models.CASCADE, related_name='categories', verbose_name="Тип")

    def __str__(self):
        return f"{self.name} ({self.cash_type.name})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Subcategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Подкатегория")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

class CashFlow(models.Model):
    date = models.DateField(default=timezone.now, verbose_name="Дата операции")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    cash_type = models.ForeignKey(CashType, on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name= "Категория")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегория")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментраий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ['-date', '-created_at']

    def clean(self):
        if self.category and self.category.cash_type != self.cash_type:
            raise ValidationError({'category': 'Выбранная категория не относится к указанному типу.'})
        
        if self.subcategory and self.subcategory.category != self.category:
            raise ValidationError({'subcategory': 'Выбранная подкатегория не относится к указанной категории'})

    def __str__(self):
        return f"{self.date} | {self.cash_type.name} | {self.amount} руб."