from django import forms

# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email_Address = forms.EmailField(required=True)
    Subject = forms.CharField(required=True)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control'})
        self.fields['Email_Address'].widget.attrs.update({'class': 'form-control'})
        self.fields['Subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['Message'].widget.attrs.update({'class': 'form-control'})

