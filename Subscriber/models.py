from django.db import models
from django.utils import timezone

class DefaultFees(models.Model):
    mosque_recoverable      = models.DecimalField("আদায়যোগ্য মসজিদের বেতন",default='200', max_digits=10, decimal_places=0, blank=True, null=True)
    graveyeard_recoverable  = models.DecimalField("আদায়যোগ্য কবরস্থানের বেতন",default='200', max_digits=10, decimal_places=0, blank=True, null=True)
    eidgah_recoverable      = models.DecimalField("আদায়যোগ্য ঈদ্গাহের বেতন",default='200', max_digits=10, decimal_places=0, blank=True, null=True)
    mustichal_recoverable   = models.DecimalField("আদায়যোগ্য মুষ্টি চালের টাকা",default='200', max_digits=10, decimal_places=0, blank=True, null=True)
    tarabih_recoverable     = models.DecimalField("আদায়যোগ্য তারাবীর টাকা",default='200', max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True

def next_serial_num():
    last_subscriber = Subscriber.objects.all().order_by('serial_num').last()
    if not last_subscriber:
        return '1'
    last_serial = last_subscriber.serial_num
    return last_serial + 1

def suggest_serial_num():
    serials = Subscriber.objects.order_by('serial_num').values_list('serial_num')
    num_of_serials = serials.count()
    last_serial = serials.last()[0]
    if last_serial == num_of_serials:
        return ""
    skipped_serials = list(range(1,int(last_serial)))
    i = 0
    while i < num_of_serials:
        current_serial = serials[i][0]
        if current_serial in skipped_serials:
            skipped_serials.remove(current_serial)
        i += 1
    txt = "Skipped serials are " + str(skipped_serials)
    return txt


class Subscriber(DefaultFees):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE,'Male'),
        (FEMALE,'Female')
    ]

    FATHER = 'FATHER'
    SPOUSE = 'SPOUSE'
    GURDIAN_TYPE_CHOICES = [
        (FATHER,'Father'),
        (SPOUSE,'Spouse')
    ]

    BLOOD_GROUP_CHOICES = [
        ('N/A','N/A'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
    ]

    MARRIED = 'MARRIED'
    UNMARRIED = 'UNMARRIED'
    MARRITAL_STATUS_CHOICES = [
        (MARRIED,'Married'),
        (UNMARRIED,'Unmarried')
    ]

    active                  = models.BooleanField(default=True, verbose_name="Active Subscriber")
    serial_num              = models.DecimalField(max_digits=4, decimal_places=0, unique=True, default=next_serial_num, help_text=suggest_serial_num)
    name                    = models.CharField(verbose_name="Full Name", max_length=255)
    date_of_birth           = models.DateField(blank=True, null=True)
    gender                  = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    num_of_family_member    = models.DecimalField(max_digits=2, decimal_places=0, help_text="You, your spouse and children if they haven't subscribed")
    gurdian_type            = models.CharField(max_length=6, choices=GURDIAN_TYPE_CHOICES, default=FATHER)
    gurdian_name            = models.CharField(max_length=255)
    identity                = models.TextField(blank=True, null=True, help_text="Relative, Clan or House")
    present_address         = models.TextField()
    permanent_address       = models.TextField()
    phone                   = models.CharField(max_length=11)
    nid_num                 = models.CharField(max_length=17, verbose_name="National Identity Number", blank=True, null=True)
    birth_certificate_num   = models.CharField(max_length=17, verbose_name="Birth Certificate Number", blank=True, null=True)
    blood_group             = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='N/A')
    marital_status          = models.CharField(max_length=9, choices=MARRITAL_STATUS_CHOICES, default=MARRIED)
    subscription_date       = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('serial_num',)

    def __str__(self):
        return str(self.serial_num) + " " + self.name

