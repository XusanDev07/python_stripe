from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

    fieldsets = (
        ('Item Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
