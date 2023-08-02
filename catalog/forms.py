from django import forms

from catalog.models import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'product_image', 'price',
                  'date_when_added', 'date_when_changed')
        # fields = '__all__'
        # exclude = ('product_image')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        if cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                            'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Такое слово использовать нельзя!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                     'бесплатно', 'обман', 'полиция', 'радар']:
            if word in cleaned_data:
                raise forms.ValidationError('Вы использовали недопустимое слово')
        return cleaned_data


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'product_image', 'price', 'date_when_changed')
        # fields = '__all__'
        # exclude = ('product_image')


