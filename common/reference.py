from django.db import models

class Division(models.TextChoices):
    """材料区分"""
    feed = 'FD', '原材料'
    part = 'PT', '部品'
    secondary = 'SD', '補助資材'
    another = 'XX', 'その他'


class Delivering(models.TextChoices):
    hand = 'HD', '手渡し'
    delivery = 'DV', '配送'
    carry = 'CR', '直接納入'
    another = 'XX', 'その他'


class Unit(models.TextChoices):
    gram = 'GR', 'グラム'
    kirogram = 'KG', 'キログラム'
    centimeter = 'CM', 'センチメートル'
    meter = 'MT', 'メートル'
    milliliter = 'ML', 'ミリリットル'
    liter = 'LT', 'リットル'
    quantity = 'QT', '個'
    sheets = 'ST', '枚'
    number = 'NU', '本'


class Settlement(models.TextChoices):
    cash = 'CA', '現金決済'
    credit = 'CC', 'クレジットカード決済'
    receivable = 'RC', '掛取引'
    another = 'AN', 'その他'


class Month(models.TextChoices):
    Jan = '1', '1月'
    Feb = '2', '2月'
    Mat = '3', '3月'
    Apl = '4', '4月'
    May = '5', '5月'
    Jon = '6', '6月'
    Jra = '7', '7月'
    Aug = '8', '8月'
    Sep = '9', '9月'
    Oct = '10', '10月'
    Nob = '11', '11月'
    Dec = '12', '12月'