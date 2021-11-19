from django.forms import ModelForm, modelformset_factory, widgets
from .models import Warehousing, Cost, Orderer, Customer, Product, Sale
from django import forms


class WarehousingForm(ModelForm):
    class Meta:
        model = Warehousing
        fields = ['material', 'quantity', 'price', 'date']


class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = [
            'term_year',
            'term_month',
            'product', 
            'product_amount',
            'material', 
            'material_amount',
            'work_in_process', 
            'defective', 
            'cost_note',
        ]
    
    # term = forms.DateField(widget=forms.SelectDateWidget(years=[x for x in range(2000, 2100)]))


class OrdererForm(ModelForm):
    class Meta:
        model = Orderer
        fields = [
            'company',
            'name',
            'tel',
            'email',
            'note',
        ]


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'company',
            'post',
            'address',
            'tel',
            'fax',
            'email',
            'note',
        ]


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = [
                'customer',
                'orderer',
                'order_date',
                'product',
                'settlement',
                'total_price',
                'sales_tax',
                'commission',
                'how_to_give',
                'giving_date',
                'post',
                'address',
                'note',
            ]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
                'item',
                'unit',
                'amount',
                'note',
            ]