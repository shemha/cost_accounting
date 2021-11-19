from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from common.reference import Division, Delivering, Unit, Settlement, Month

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
                regex='^[0-9]+$',
                message='７桁の数字を入力してください。'
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
                regex='^[0-9]+$',
                message='10桁以上の数字を入力してください。'
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
                regex='^[0-9]+$',
                message='10桁の数字を入力してください。'
            )
        ]
    )
    email = models.EmailField(
        'メールアドレス',
        blank=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$',
                message='無効な文字列が入っています。'
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
    division = models.CharField('区分', max_length=2, choices=Division.choices)
    unit = models.CharField('単位', max_length=2, choices=Unit.choices)
    vender = models.ForeignKey(Vender, verbose_name='仕入先', on_delete=models.PROTECT)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    """品目マスタ"""
    name = models.CharField('品名', max_length=100, unique=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', on_delete=models.PROTECT)
    unit = models.CharField('単位', max_length=2, choices=Unit.choices)
    entry = models.DateTimeField('登録日', auto_now=True)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """販売製品"""
    item = models.ForeignKey(Item, verbose_name='品名', on_delete=models.PROTECT)
    unit = models.CharField('単位', max_length=2, choices=Unit.choices)
    amount = models.PositiveIntegerField('セット数')
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.item.name


class Cost(models.Model):
    """原価マスタ"""
    product = models.ForeignKey(Product, verbose_name='製品名', on_delete=models.PROTECT)
    product_amount = models.FloatField('生産量', validators=[MinValueValidator(0)], default=0)
    material = models.ForeignKey(Material, verbose_name='材料名', on_delete=models.PROTECT)
    material_amount = models.FloatField('消費量', validators=[MinValueValidator(0)], default=0)
    work_in_process = models.FloatField('仕掛量', validators=[MinValueValidator(0)], null=True, blank=True)
    defective = models.FloatField('仕損じ量', validators=[MinValueValidator(0)], null=True, blank=True)
    term_year = models.CharField('開始年度', max_length=4)
    term_month = models.CharField('開始月', max_length=2, choices=Month.choices)
    cost_note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.product.item.name


class Warehousing(models.Model):
    """入庫マスタ"""
    material = models.ForeignKey(Material, verbose_name='材料名', on_delete=models.PROTECT)
    date = models.DateField('入庫日')
    quantity = models.FloatField('数量', validators=[MinValueValidator(0)], default=0)
    price = models.FloatField('税抜価額', validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.material.name

        # return str(self.material)

    # class Mata:
    #     db_table = 'warehousing'


class Stock(models.Model):
    """期末在庫マスタ"""
    warehousing = models.ForeignKey(Warehousing, verbose_name='材料名', on_delete=models.PROTECT)
    inventory = models.FloatField('仕入数量', validators=[MinValueValidator(0)], default=0)
    note = models.TextField('備考', blank=True)


class Customer(models.Model):
    """得意先マスタ"""
    company = models.CharField('会社名', max_length=100)
    post = models.CharField(
        '郵便番号',
        max_length=7,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex='^[0-9]+$',
                message='７桁の数字を入力してください。'
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
                regex='^[0-9]+$',
                message='10桁以上の数字を入力してください。'
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
                regex='^[0-9]+$',
                message='10桁の数字を入力してください。'
            )
        ]
    )
    email = models.EmailField(
        'メールアドレス',
        blank=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$',
                message='無効な文字列が入っています。'
            )
        ]
    )
    entry = models.DateTimeField('登録日', auto_now=True)
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.company


class Orderer(models.Model):
    """発注者マスタ"""
    company = models.ForeignKey(Customer, verbose_name='会社名', on_delete=models.PROTECT)
    name = models.CharField('担当者名', max_length=50)
    tel = models.CharField(
        '電話番号',
        blank=True,
        max_length=11,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex='^[0-9]+$',
                message='10桁の数字を入力してください。'
            )
        ]
    )
    email = models.EmailField(
        'メールアドレス',
        blank=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$',
                message='無効な文字列が入っています。'
            )
        ]
    )
    note = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    """販売テーブル"""
    customer = models.ForeignKey(Customer, verbose_name='得意先', on_delete=models.PROTECT)
    orderer = models.ForeignKey(Orderer, verbose_name='得意先', on_delete=models.PROTECT)
    order_date = models.DateField('注文日')
    product = models.ForeignKey(Product, verbose_name='製品名', on_delete=models.PROTECT)
    order_amount = models.PositiveIntegerField('注文数', default=0)
    settlement = models.CharField('決済方法', max_length=2, choices=Settlement.choices)
    total_price = models.PositiveIntegerField('販売単価')
    sales_tax = models.PositiveIntegerField('消費税額')
    commission = models.PositiveIntegerField('1製品あたりの手数料')
    how_to_give = models.CharField('引き渡し方法', max_length=2, choices=Delivering.choices)
    giving_date = models.DateTimeField('引き渡し日')
    post = models.CharField(
        '郵便番号',
        blank=True,
        max_length=7,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex='^[0-9]+$',
                message='７桁の数字を入力してください。'
            )
        ]
    )
    address = models.CharField('住所', max_length=100, blank=True)
    note = models.TextField('備考', blank=True)
    
    def __str__(self):
        return self.order_date