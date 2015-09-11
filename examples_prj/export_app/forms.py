from django import forms


class ContactForm(forms.Form):
    # name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)
    created_at = forms.DateTimeField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
