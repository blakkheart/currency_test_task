from django.http import JsonResponse
from currency.models import Currency


def test_view(request):
    # хранить дату в моделе как дату, преобразовывать на выходе
    charcode = request.GET.get('charcode')
    date = request.GET.get('date')
    currency_obj = Currency.objects.get(date=date)
    rate = getattr(currency_obj, charcode)
    return JsonResponse({
        'charcode': charcode,
        'date': date,
        'rate': rate,
    })
