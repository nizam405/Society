from django import forms
from .models import Subscriber, suggest_serial_num

class SubscriberForm(forms.ModelForm):
    # serial_num = forms.CharField(help_text=suggest_serial_num)
    class Meta:
        model = Subscriber
        fields = [
            'active','serial_num', 'name', 'date_of_birth', 'gender',
            'num_of_family_member', 'gurdian_type', 'gurdian_name', 'present_address', 
            'permanent_address', 'additional_info', 'phone', 'nid_num', 
            'birth_certificate_num', 'blood_group', 'marital_status', 'subscription_date',
            'mosque_recoverable', 'graveyeard_recoverable', 'eidgah_recoverable',
            'mustichal_recoverable', 'tarabih_recoverable'
        ]
        widgets = {
            'gender'            : forms.RadioSelect(),
            'gurdian_type'      : forms.RadioSelect(),
            'present_address'   : forms.Textarea(attrs={'rows':2}),
            'permanent_address' : forms.Textarea(attrs={'rows':2}),
            'additional_info'   : forms.Textarea(attrs={'rows':2}),
        }
