from django.contrib import admin

from .models import Product, NetworkNode

# Register your models here.

admin.site.register(Product)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    raw_id_fields = ('supplier',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
        self.message_user(request, "Debt successfully cleared.")

    clear_debt.short_description = "Clear debt fo selected network nodes"
