from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField()
    subject = forms.CharField(label='Assunto')
    message = forms.CharField(help_text='Write here your message!', max_length=500, widget=forms.Textarea())