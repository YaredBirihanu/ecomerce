from django.contrib import admin
from .models import Category,Product,Customer,Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')
