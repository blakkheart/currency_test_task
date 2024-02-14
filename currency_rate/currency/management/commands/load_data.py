import json
from typing import Any
from datetime import datetime

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
        date_corr_format = datetime.strptime(date, '%Y-%m-%d').date()
        valutes = data.get('Valute')
        model = Currency(date=date_corr_format)
        for valute in valutes:
            nominal = valutes.get(valute).get('Nominal')
            value = valutes.get(valute).get('Value')
            setattr(model, valute, value/nominal)
        model.save()
        print('Done!')
