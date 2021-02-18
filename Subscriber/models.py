from django.db import models
from django.utils import timezone

from .choices import gender_choices, gurdian_type_choices, blood_group_choices, marital_status_choices

def next_serial_num():
    last_subscriber = Subscriber.objects.all().order_by('serial_num').last()
    if not last_subscriber:
        return '1'
    last_serial = last_subscriber.serial_num
    return last_serial + 1

# def suggest_serial_num():
#     serials = Subscriber.objects.values_list('serial_num')
#     num_of_serials = serials.count()
#     last_serial = serials.last()[0]
#     if last_serial == num_of_serials:
#         return ""
#     skipped_serials = []
#     i = 1
#     while i <= last_serial:
#         if i != serials[i][0]:
#             skipped_serials.append(i)
#             i += 1
#         i += 1
#     txt = "Skipped serials are" + skipped_serials
#     return txt


class Subscriber(models.Model):
    active                  = models.BooleanField(default=True, verbose_name="Active Subscriber")
    serial_num              = models.DecimalField(max_digits=4, decimal_places=0, unique=True, default=next_serial_num)
    name                    = models.CharField(verbose_name="Full Name", max_length=255)
    date_of_birth           = models.DateField(blank=True, null=True)
    gender                  = models.CharField(max_length=6, choices=gender_choices, default='Male')
    num_of_family_member    = models.DecimalField(max_digits=2, decimal_places=0, help_text="You, your spouse and children if they haven't subscribed")
    gurdian_type            = models.CharField(max_length=6, choices=gurdian_type_choices, default='Father')
    gurdian_name            = models.CharField(max_length=255)
    identity                = models.TextField(blank=True, null=True, help_text="Relative, Clan or House")
    present_address         = models.TextField()
    permanent_address       = models.TextField()
    phone                   = models.CharField(max_length=11)
    nid_num                 = models.CharField(max_length=17, verbose_name="National Identity Number", blank=True, null=True)
    birth_certificate_num   = models.CharField(max_length=17, verbose_name="Birth Certificate Number", blank=True, null=True)
    blood_group             = models.CharField(max_length=3, choices=blood_group_choices, default='N/A')
    marital_status          = models.CharField(max_length=9, choices=marital_status_choices, default='Married')
    subscription_date       = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('serial_num',)

    def __str__(self):
        return str(self.serial_num) + " " + self.name

