from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Warehousing


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

class WarehousingForm(ModelForm):
    class Meta:
        model = Warehousing
        fields = ['material', 'quantity', 'unit', 'date']