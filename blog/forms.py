from django import forms

class Subscribe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'name'}))
    Email = forms.EmailField(required=True)
    subject = forms.CharField(label='Assunto',required=True)
    message = forms.CharField(label='Escreva sua mensagem!', max_length=500, widget=forms.Textarea(), required=True)
    Email.widget.attrs.update({'class': 'form-control','id':'email'})
    subject.widget.attrs.update({'class': 'form-control','id':'subject'})
    message.widget.attrs.update({'class': 'form-control','id':'message'})