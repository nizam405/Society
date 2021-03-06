from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['active','serial_num', 'name', 'date_of_birth', 'gender',
        'num_of_family_member', 'gurdian_type', 'gurdian_name', 'identity', 
        'present_address', 'permanent_address', 'phone', 'nid_num', 
        'birth_certificate_num', 'blood_group', 'marital_status', 'subscription_date',
        'mosque_recoverable', 'graveyeard_recoverable', 'eidgah_recoverable',
        'mustichal_recoverable', 'tarabih_recoverable']
