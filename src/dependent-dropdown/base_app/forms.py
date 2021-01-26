from django import forms
from .models import Person, City
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"class": "form-control my-2", "placeholder": "Enter Full Name"})
        self.fields['city'].widget.attrs.update({"class": "form-control my-2"})
        self.fields['country'].widget.attrs.update({"class": "form-control my-2"})
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = self.data.get('country')
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

    # def clean(self):
    #     name = self.cleaned_data['name']
    #     try:
    #         person = Person.objects.get(name=name)
    #         print("exists")
    #         raise forms.ValidationError("Name Exists")
    #     except ObjectDoesNotExist:
    #         pass
    #     return self.cleaned_data

    
    class Meta:
        model = Person
        fields = '__all__'