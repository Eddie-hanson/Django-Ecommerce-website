from django.forms import forms
from .models import User_FeedBack


class UserFeedbackForm(forms.ModelForm):

    class Meta:
        model = User_FeedBack
        fields = ('__All__')
    widgets = {'Name': forms.TextInput(attrs={'class': 'contact_input contact_input_name inpt', 'type': 'text', 'placeholder': 'Your Name', 'required': "required"}),
               'Subject': forms.TextInput(attrs={'class': 'contact_input contact_input_subject inpt', 'type': 'text', 'placeholder': 'Subject', 'required': "required"}),
               'email': forms.EmailInput(attrs={'class': 'contact_input contact_input_email inpt', 'type': 'text', 'placeholder': 'Your E-mail', 'required': "required"}),
               'Message': forms.TextInput(attrs={'class': 'contact_textarea contact_input inpt', 'type': "text", 'placeholder': 'Message', 'required': "required"}),
               }
