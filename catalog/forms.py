from django import forms
from catalog.models import Product, Version


class MixinStyle:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductAddForm(MixinStyle, forms.ModelForm):
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


class ProductEditForm(MixinStyle, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'product_image', 'price', 'date_when_changed', 'is_active')

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


class VersionCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_version_number(self):
    #     cleaned_data = self.cleaned_data['version_number']
    #     existing_versions = [version.version_number for version in Version.objects.filter(product=self.cleaned_data['product'])]
    #     if cleaned_data in existing_versions:
    #         raise forms.ValidationError('Такая версия недопустима!')
    #     return cleaned_data
