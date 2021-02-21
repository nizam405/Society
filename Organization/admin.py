from django.contrib import admin

from .models import SubscriptionFee, Revenue, Expense

admin.site.register(SubscriptionFee)
admin.site.register(Revenue)
admin.site.register(Expense)
