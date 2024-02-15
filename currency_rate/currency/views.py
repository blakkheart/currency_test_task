from datetime import datetime

from django.http import JsonResponse

from currency.models import Currency

CHARCODE_SET = (
    'AUD',
    'AZN',
    'GBP',
    'AMD',
    'BYN',
    'BGN',
    'BRL',
    'HUF',
    'VND',
    'HKD',
    'GEL',
    'DKK',
    'AED',
    'USD',
    'EUR',
    'EGP',
    'INR',
    'IDR',
    'KZT',
    'CAD',
    'QAR',
    'KGS',
    'CNY',
    'MDL',
    'NZD',
    'NOK',
    'PLN',
    'RON',
    'XDR',
    'SGD',
    'TJS',
    'THB',
    'TRY',
    'TMT',
    'UZS',
    'UAH',
    'CZK',
    'SEK',
    'CHF',
    'RSD',
    'ZAR',
    'KRW',
    'JPY',
)


def rate(request) -> JsonResponse:
    charcode = request.GET.get('charcode')
    if not charcode or charcode not in CHARCODE_SET:
        return JsonResponse({
            'error': ' You should pick one of the available charcodes!',
            'charcode_list': CHARCODE_SET,
        })
    date = request.GET.get('date')
    if not date:
        return JsonResponse({
            'error': 'You should choose the date!'
        })
    try:
        date_corr_format = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({
            'error': 'Date must be the correct format %Y-%m-%d!',
            'example': '2024-02-13'
        })
    currency_obj = Currency.objects.filter(date=date_corr_format).first()
    rate = getattr(currency_obj, charcode)
    if not rate:
        rate = 'No data'
    return JsonResponse({
        'charcode': charcode,
        'date': date,
        'rate': rate,
    })
