from django import forms
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ContactForm(forms.Form):
    # name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)
    desde = forms.DateTimeField(widget=DateInput())
    hasta = forms.DateTimeField(widget=DateInput())

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
