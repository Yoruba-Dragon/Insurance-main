from django.contrib import admin
from .models import Policy

# Register your models here.
admin.site.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'policy_type', 'provider_name', 'expiry_date', 'reminder_date')
    search_fields = ('policy_number', 'provider_name')
    list_filter = ('policy_type',)
