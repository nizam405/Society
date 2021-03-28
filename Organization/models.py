from django.db import models
from django.utils import timezone
import datetime

from Subscriber.models import Subscriber, DefaultFees
from .choices import revenue_type_choices, sources

class SubscriptionFee(DefaultFees):
    date                    = models.DateField(default=timezone.now)
    subscriber              = models.ForeignKey(to=Subscriber, on_delete=models.CASCADE)
    year                    = models.CharField("হিসাব কাল", max_length=4, default=datetime.datetime.today().year)
    
    mosque_recovered        = models.DecimalField("আদায়কৃত মসজিদের বেতন", max_digits=10, decimal_places=0, blank=True, null=True)
    graveyeard_recovered    = models.DecimalField("আদায়কৃত কবরস্থানের বেতন", max_digits=10, decimal_places=0, blank=True, null=True)
    eidgah_recovered        = models.DecimalField("আদায়কৃত ঈদ্গাহের বেতন", max_digits=10, decimal_places=0, blank=True, null=True)
    mustichal_recovered     = models.DecimalField("আদায়কৃত মুষ্টি চালের টাকা", max_digits=10, decimal_places=0, blank=True, null=True)
    tarabih_recovered       = models.DecimalField("আদায়কৃত তারাবীর টাকা", max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        unique_together = ('subscriber','year')
        ordering = ('subscriber__serial_num',)
    
    def sum(self):
        total = 0
        if self.mosque_recovered != None:
            total += self.mosque_recovered 
        if self.graveyeard_recovered != None:
            total += self.graveyeard_recovered 
        if self.eidgah_recovered != None:
            total += self.eidgah_recovered 
        if self.mustichal_recovered != None:
            total += self.mustichal_recovered 
        if self.tarabih_recovered != None:
            total += self.tarabih_recovered 
        return total
    
    def default_fees(self):
        total = 0
        if datetime.date.today() >= datetime.date(datetime.datetime.now().year,6,1):
            if self.mosque_recoverable != None:
                total += self.mosque_recoverable 
            if self.graveyeard_recoverable != None:
                total += self.graveyeard_recoverable 
        if self.eidgah_recoverable != None:
            total += self.eidgah_recoverable 
        if self.mustichal_recoverable != None:
            total += self.mustichal_recoverable 
        if self.tarabih_recoverable != None:
            total += self.tarabih_recoverable 
        return total
    
    def due(self):
        return int(self.default_fees()) - int(self.sum())

    def __str__(self):
        return str(self.subscriber.serial_num) + " - " + self.subscriber.name + " (" + self.year + ")"

class Revenue(models.Model):
    date            = models.DateField(default=timezone.now)
    # unknown = models.BooleanField()
    revenue_type    = models.CharField(max_length=10, choices=revenue_type_choices)
    subscriber      = models.ForeignKey(to=Subscriber, on_delete=models.CASCADE, blank=True, null=True)
    description     = models.TextField()
    amount          = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.date) + " - " + self.description + " (" + str(self.amount) + ")"

class Expense(models.Model):
    date        = models.DateField(default=timezone.now)
    source      = models.CharField(max_length=10, choices=sources)
    voucher_no  = models.CharField(max_length=10)
    description = models.TextField()
    amount      = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.source + " - " + self.description + " (" + str(self.amount) + ")"