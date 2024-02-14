from django.contrib import admin
from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', )
    list_filter = ('date', )
    search_fields = ('date', )
    list_per_page = 25


admin.site.site_header = 'Currency admin panel'
admin.site.site_title = 'Currency'
admin.site.index_title = 'Currency models control'
