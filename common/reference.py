from django.db import models

class Division(models.TextChoices):
    """材料区分"""
    feed = 'F', '原材料'
    part = 'P', '部品'
    secondary = 'S', '補助資材'
    another = 'X', 'その他'


class Shipping(models.TextChoices):
    hand = 'H', '手渡し'
    delivery = 'D', '配送'
    carry = 'C', '搬入'
    another = 'X', 'その他'


class Unit(models.TextChoices):
    gram = 'GR', 'グラム'
    kirogram = 'KG', 'キログラム'
    centimeter = 'CM', 'センチメートル'
    meter = 'MT', 'メートル'
    milliliter = 'ML', 'ミリリットル'
    liter = 'LT', 'リットル'
    quantity = 'QT', '個数'


class Settlement(models.TextChoices):
    cash = 'CA', '現金決済'
    credit = 'CC', 'クレジットカード決済'
    receivable = 'RC', '掛取引'
    another = 'AN', 'その他'