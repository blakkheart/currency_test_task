import json
from typing import Any
import requests
from django.core.management import BaseCommand

from currency.models import Currency


class Command(BaseCommand):
    """Менеджмент команда для выгрузки данных с API."""

    def handle(self, *args: Any, **options: Any) -> None:
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        status = r.status_code
        if status != 200:
            raise ConnectionError('Апи недоступно!')
        data = r.json()
        date = data.get('Date').split('T')[0]
        # обработать дату и записать в модель
        valutes = data.get('Valute')
        model = Currency(date=date)
        for valute in valutes:
            nominal = valutes.get(valute).get('Nominal')
            value = valutes.get(valute).get('Value')
            setattr(model, valute, value/nominal)
            # print(valute, end=' ')
            # print(valutes.get(valute).get('Value'))

        model.save()
        print('Done!')
