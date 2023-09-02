from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=256,
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
                                  required=False)
    price = forms.DecimalField(required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-control-sm'}))
