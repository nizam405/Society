from django.db import models
from django.utils import timezone
import datetime

from Subscriber.models import Subscriber
from .choices import revenue_type_choices, sources

class SubscriptionFee(models.Model):
    date = models.DateField(default=timezone.now)
    subscriber = models.ForeignKey(to=Subscriber, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, default=datetime.datetime.today().year, verbose_name="হিসাব কাল")
    mosque = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="মসজিদ")
    graveyeard = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="কবরস্থান")
    eidgah = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="ঈদ্গাহ")
    mustichal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="মুষ্টি চাল")
    tarabih = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="তারাবীহ")

    class Meta:
        unique_together = ('subscriber','year')

    def __str__(self):
        return self.subscriber.name + " (" + self.year + ")"

class Revenue(models.Model):
    date = models.DateField(default=timezone.now)
    # unknown = models.BooleanField()
    revenue_type = models.CharField(max_length=10, choices=revenue_type_choices)
    subscriber = models.ForeignKey(to=Subscriber, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description + " (" + str(self.amount) + ")"

class Expense(models.Model):
    date = models.DateField(default=timezone.now)
    source = models.CharField(max_length=10, choices=sources)
    voucher_no = models.CharField(max_length=10)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.source + " - " + self.description + " (" + str(self.amount) + ")"