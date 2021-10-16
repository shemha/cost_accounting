from django.forms import ModelForm, modelformset_factory
from .models import *


class WarehousingForm(ModelForm):
    class Meta:
        model = Warehousing
        fields = ['material', 'quantity', 'price', 'date']

class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = [
            'product', 
            'product_amount',
            'material', 
            'material_amount',
            'work_in_process', 
            'defective', 
            'term_begin', 
            'term_end', 
            'cost_note',
        ]


class OrdererForm(ModelForm):
    model = Orderer
    fields = [
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