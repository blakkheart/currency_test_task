from datetime import datetime

from django.http import JsonResponse

from currency.models import Currency


def rate(request) -> JsonResponse:
    charcode = request.GET.get('charcode')
    date = request.GET.get('date')
    date_corr_format = datetime.strptime(date, '%Y-%m-%d').date()
    currency_obj = Currency.objects.filter(date=date_corr_format).first()
    rate = getattr(currency_obj, charcode)
    if not rate:
        rate = 'No data'
    return JsonResponse({
        'charcode': charcode,
        'date': date,
        'rate': rate,
    })
