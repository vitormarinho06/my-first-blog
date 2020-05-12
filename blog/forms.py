from django import forms

class Subscribe(forms.Form):
    name = forms.CharField(max_length=100)
    Email = forms.EmailField(required=True)
    subject = forms.CharField(label='Assunto',required=True)
    message = forms.CharField(label='Escreva sua mensagem!', max_length=500, widget=forms.Textarea(), required=True)