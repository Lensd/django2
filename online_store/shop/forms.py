from django import forms
from .models import Order, Review, RATE_CHOICES
from .bulma_mixin import BulmaMixin


class OrderForm(BulmaMixin, forms.ModelForm):
    address = forms.CharField(label='Write address')
    phone = forms.CharField(label='Write Phone')

    class Meta:
        model = Order
        fields = ['address', 'phone']


class RateForm(forms.ModelForm,  BulmaMixin):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='leave your review here')
    rate = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Rate product from 1 to 5')

    class Meta:
        model = Review
        fields = ['text', 'rate']
