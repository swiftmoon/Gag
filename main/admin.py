from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name_uz','name_ru']
    class Meta:
        model = Category
