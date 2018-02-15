import time
from django import forms

# our new form
from page.notify import Notify


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mail_object = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    def send_contact_mail(self, request):
        cd = self.cleaned_data

        message = Notify(
            template="emails/contact_mail",
            subject=cd.get("mail_object"),
            sender=cd.get("email"),
            receiver="sergio.casolari@scasolari.com",
            request_context=request,
            data={
                'text': cd.get("text"),
                'name': cd.get("name"),
                'email': cd.get("email"),
                'message_time': time.strftime("%H:%M:%S"),
                'message_date': time.strftime("%d/%m/%Y"),
            },
        )
        message.send()

        return True


#    def __init__(self, *args, **kwargs):
#        super(ContactForm, self).__init__(*args, **kwargs)
#        self.fields['Name'].widget.attrs.update({'class': 'form-control'})
#        self.fields['Email_Address'].widget.attrs.update({'class': 'form-control'})
#        #self.fields['Subject'].widget.attrs.update({'class': 'form-control'})
#        self.fields['Message'].widget.attrs.update({'class': 'form-control', 'rows': '4',})

