from django import forms


class ObjectAdFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({
            'placeholder': 'мин и макс цена'
        })
