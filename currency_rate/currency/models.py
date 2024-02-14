from django.db import models


class Currency(models.Model):
    '''Хранит данные о валюте на определенную дату.'''
    date = models.CharField(max_length=20)
    AUD = models.FloatField()
    AZN = models.FloatField()
    GBP = models.FloatField()
    AMD = models.FloatField()
    BYN = models.FloatField()
    BGN = models.FloatField()
    BRL = models.FloatField()
    HUF = models.FloatField()
    VND = models.FloatField()
    HKD = models.FloatField()
    GEL = models.FloatField()
    DKK = models.FloatField()
    AED = models.FloatField()
    USD = models.FloatField()
    EUR = models.FloatField()
    EGP = models.FloatField()
    INR = models.FloatField()
    IDR = models.FloatField()
    KZT = models.FloatField()
    CAD = models.FloatField()
    QAR = models.FloatField()
    KGS = models.FloatField()
    CNY = models.FloatField()
    MDL = models.FloatField()
    NZD = models.FloatField()
    NOK = models.FloatField()
    PLN = models.FloatField()
    RON = models.FloatField()
    XDR = models.FloatField()
    SGD = models.FloatField()
    TJS = models.FloatField()
    THB = models.FloatField()
    TRY = models.FloatField()
    TMT = models.FloatField()
    UZS = models.FloatField()
    UAH = models.FloatField()
    CZK = models.FloatField()
    SEK = models.FloatField()
    CHF = models.FloatField()
    RSD = models.FloatField()
    ZAR = models.FloatField()
    KRW = models.FloatField()
    JPY = models.FloatField()

    def __str__(self):
        return f'Currency on the date of {self.date}'


""""
Валюта - модель
у нее есть дата - по ней мы будем отадвать пользователю актуальные на момент даты данные
поле навзание - навзание валюты, а число - это посчитанный курс относительно рубля 

"""
