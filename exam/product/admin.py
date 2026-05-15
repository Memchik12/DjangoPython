from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'set_type', 'material', 'race_type', 'miniatures_count')
    list_filter = ('material', 'race_type', 'set_type')
    search_fields = ('title',)
# Register your models here.
