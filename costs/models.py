from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from common.reference import Division, Shipping, Unit, Settlement

# Create your models here.
class Vender(models.Model):
    """仕入先マスタ"""
    company = models.CharField('会社名', max_length=100, blank=True)
    name = models.CharField('担当者名', max_length=50)
    post = models.CharField(
        '郵便番号',
        max_length=7,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex="^[0-9]+$",
                message="７桁の数字を入力してください。"
            )
        ]
    )
    address = models.CharField('住所', max_length=100)
    tel = models.CharField(
        '電話番号',
        max_length=11,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex="^[0-9]+$",
                message="10桁以上の数字を入力してください。"
            )
        ]
    )
    fax = models.CharField(
        'FAX番号',
        blank=True,
        max_length=10,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex="^[0-9]+$",
                message="10桁の数字を入力してください。"
            )
        ]
    )
    email = models.EmailField(
        'メールアドレス',
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$",
                message="無効な文字列が入っています。"
            )
        ]
    )
    entry = models.DateTimeField('登録日', auto_now=True)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    """材料マスタ"""
    name = models.CharField('材料名', max_length=100)
    division = Division.choices
    vender = models.ForeignKey(Vender, on_delete=models.PROTECT)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    """製品マスタ"""
    name = models.CharField('製品名', max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    division = Shipping.choices
    unit = Unit.choices
    amount = models.PositiveIntegerField("セット数")
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Cost(models.Model):
    """原価マスタ"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    amount = models.FloatField('使用量', validators=[MinValueValidator(0)], default=0)
    work_in_process = models.FloatField('仕掛量', validators=[MinValueValidator(0)], default=0)
    defective = models.FloatField('仕損じ量', validators=[MinValueValidator(0)], default=0)
    term_begin = models.DateTimeField('開始日', auto_now=True)
    term_end = models.DateTimeField('締め日', auto_now=True)
    cost_note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.product


class Warehousing(models.Model):
    """入庫マスタ"""
    cost = models.ForeignKey(Cost, on_delete=models.PROTECT)
    date = models.DateTimeField('入庫日', auto_now=True)
    quantity = models.FloatField('入庫量', validators=[MinValueValidator(0)], default=0)
    unit = models.FloatField('単価', validators=[MinValueValidator(0)], default=0)


class Stock(models.Model):
    """期末在庫マスタ"""
    warehousing = models.ForeignKey(Warehousing, on_delete=models.PROTECT)
    inventory = models.FloatField('仕入数量', validators=[MinValueValidator(0)], default=0)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.warehousing


class Client(models.Model):
    """顧客マスタ"""
    company = models.CharField('会社名', max_length=100)
    name = models.CharField('担当者名', max_length=50)
    post = models.CharField(
        '郵便番号',
        max_length=7,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex="^[0-9]+$",
                message="７桁の数字を入力してください。"
            )
        ]
    )
    address = models.CharField('住所', max_length=100)
    tel = models.CharField(
        '電話番号',
        max_length=11,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex="^[0-9]+$",
                message="10桁以上の数字を入力してください。"
            )
        ]
    )
    fax = models.CharField(
        'FAX番号',
        blank=True,
        max_length=10,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex="^[0-9]+$",
                message="10桁の数字を入力してください。"
            )
        ]
    )
    email = models.EmailField(
        'メールアドレス',
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$",
                message="無効な文字列が入っています。"
            )
        ]
    )
    entry = models.DateTimeField('登録日', auto_now=True)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    """販売テーブル"""
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    order_date = models.DateTimeField('注文日', auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_amount = models.PositiveIntegerField("注文数", default=0)
    settlement = Settlement.choices
    total_price = models.PositiveIntegerField("販売価額")
    sales_tax = models.PositiveIntegerField("消費税額")
    commission = models.PositiveIntegerField("その他手数料")
    how_to_give = models.PositiveIntegerField("引き渡し方法")
    giving_date = models.DateTimeField('引き渡し日', auto_now=True)
    
    def __str__(self):
        return self.order_date