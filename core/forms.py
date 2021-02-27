from django import forms
from localflavor.br.forms import BRStateChoiceField, BRZipCodeField, BRCPFField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    CPF = BRCPFField(label='CPF')
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Avenida Paulista 123'
    }), label='Endereço', max_length=100)

    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Apt. 10'
    }),required=False, label='Ap, Cond. (opcional)', max_length=100)

    state = BRStateChoiceField(label='Estado')

    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'São Paulo',
    }), label='Cidade', max_length=100)

    # CEP = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': '13165-000'
    # }), label='CEP')

    CEP = BRZipCodeField(label='CEP', max_length=9)


    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(), label='Mesmo Endereço de Cobrança', required=False)

    save_info = forms.BooleanField(widget=forms.CheckboxInput(), label='Salvar Informação', required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES, label='Opções de Pagamento', required=True)


    