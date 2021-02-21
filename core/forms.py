from django import forms

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Avenida Paulista 123'
    }), label='Endereço')
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Apt. 10'
    }),required=False, label='Ap, Cond. (opcional)' )
    state = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'São Paulo'
    }),label='Estado')
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'São Paulo'
    }), label='São Paulo')
    CEP = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '13165-000'
    }), label='CEP')
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(), label='Mesmo Endereço de Cobrança', required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(), label='Salvar Informação', required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES, label='Opções de Pagamento')

    