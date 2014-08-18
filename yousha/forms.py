from django import forms

class SendMailForm(forms.Form):
    src_email = forms.CharField()
    dest_email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

