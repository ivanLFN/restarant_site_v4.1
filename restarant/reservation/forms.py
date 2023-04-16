from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    