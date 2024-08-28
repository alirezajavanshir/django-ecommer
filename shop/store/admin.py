from django.contrib import admin
from .models import Category, Product, Customer, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name", "description")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("product", "customer", "quantity", "date", "status")
    list_filter = ("status", "date")


# ثبت مدل‌ها با تنظیمات خاص
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
