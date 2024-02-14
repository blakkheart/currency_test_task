from django.contrib import admin
from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_filter = ('date', )
    search_fields = ('date', )
    list_per_page = 25
