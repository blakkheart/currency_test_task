from django.db import models


class Currency(models.Model):
    '''Хранит данные о валюте на определенную дату.'''
    date = models.DateField(auto_now=False, auto_now_add=False)
    AUD = models.DecimalField(
        help_text='Австралийский доллар',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    AZN = models.DecimalField(
        help_text='Азербайджанский манат',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    GBP = models.DecimalField(
        help_text='Фунт стерлингов Соединенного королевства',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    AMD = models.DecimalField(
        help_text='Армянских драмов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    BYN = models.DecimalField(
        help_text='Белорусский рубль',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    BGN = models.DecimalField(
        help_text='Болгарский лев',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    BRL = models.DecimalField(
        help_text='Бразильский реал',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    HUF = models.DecimalField(
        help_text='Венгерских форинтов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    VND = models.DecimalField(
        help_text='Вьетнамских донгов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    HKD = models.DecimalField(
        help_text='Гонконгский доллар',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    GEL = models.DecimalField(
        help_text='Грузинский лари',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    DKK = models.DecimalField(
        help_text='Датская крона',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    AED = models.DecimalField(
        help_text='Дирхам ОАЭ',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    USD = models.DecimalField(
        help_text='Доллар США',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    EUR = models.DecimalField(
        help_text='Евро',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    EGP = models.DecimalField(
        help_text='Египетских фунтов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    INR = models.DecimalField(
        help_text='Индийских рупий',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    IDR = models.DecimalField(
        help_text='Индонезийских рупий',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    KZT = models.DecimalField(
        help_text='Казахстанских тенге',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    CAD = models.DecimalField(
        help_text='Канадский доллар',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    QAR = models.DecimalField(
        help_text='Катарский риал',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    KGS = models.DecimalField(
        help_text='Киргизских сомов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    CNY = models.DecimalField(
        help_text='Китайский юань',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    MDL = models.DecimalField(
        help_text='Молдавских леев',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    NZD = models.DecimalField(
        help_text='Новозеландский доллар',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    NOK = models.DecimalField(
        help_text='Норвежских крон',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    PLN = models.DecimalField(
        help_text='Польский злотый',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    RON = models.DecimalField(
        help_text='Румынский лей',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    XDR = models.DecimalField(
        help_text='СДР (специальные права заимствования)',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    SGD = models.DecimalField(
        help_text='Сингапурский доллар',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    TJS = models.DecimalField(
        help_text='Таджикских сомони',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    THB = models.DecimalField(
        help_text='Таиландских батов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    TRY = models.DecimalField(
        help_text='Турецких лир',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    TMT = models.DecimalField(
        help_text='Новый туркменский манат',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    UZS = models.DecimalField(
        help_text='Узбекских сумов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    UAH = models.DecimalField(
        help_text='Украинских гривен',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    CZK = models.DecimalField(
        help_text='Чешских крон',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    SEK = models.DecimalField(
        help_text='Шведских крон',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    CHF = models.DecimalField(
        help_text='Швейцарский франк',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    RSD = models.DecimalField(
        help_text='Сербских динаров',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    ZAR = models.DecimalField(
        help_text='Южноафриканских рэндов',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    KRW = models.DecimalField(
        help_text='Вон Республики Корея',
        max_digits=12, decimal_places=4, null=True, blank=True
    )
    JPY = models.DecimalField(
        help_text='Японских иен',
        max_digits=12, decimal_places=4, null=True, blank=True
    )

    def __str__(self):
        return f'Currency on the date of {self.date}'
