from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    messages = forms.CharField(widget=forms.Textarea, required=True)