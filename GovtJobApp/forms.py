from django import forms

class ForestDropdownForm(forms.Form):
    choices = (
        ('--select--','--select--'),
        ('HYDERABAD','HYDERABAD'),
        ('BANGLORE','BANGLORE')
    )
    select=forms.ChoiceField(
        choices=choices,
        widget=forms.Select(),
        # required=True,
        label='select location'
    )

    choices1 = (
        ('--select--','--select--'),
        ('BTECH','BETCH'),
        ('12th','12th')
    )
    select_qualification=forms.ChoiceField(
        choices=choices1,
        widget=forms.Select(),
        # required=True,
        label="select qualification"
    )
    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(),
    )