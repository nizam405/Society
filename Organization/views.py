import datetime
from django.shortcuts import render
from django.db.models import Sum
from .models import SubscriptionFee, Revenue, Expense
from Subscriber.models import Subscriber

# Create your views here.
def SubscriptionFees(request):
    subscribers = Subscriber.objects.all()
    # fees = SubscriptionFee.objects.all()
    for subscriber in subscribers:
        if subscriber.active == True:
            sub_year = subscriber.subscription_date.year
            current_year = datetime.datetime.now().year

            for year in range(sub_year,current_year+2):
                fee, created = SubscriptionFee.objects.get_or_create(
                    subscriber=subscriber, 
                    year=year,
                    defaults={
                            'mosque_recoverable': subscriber.mosque_recoverable,
                            'graveyeard_recoverable':subscriber.graveyeard_recoverable,
                            'eidgah_recoverable':subscriber.eidgah_recoverable,
                            'mustichal_recoverable':subscriber.mustichal_recoverable,
                            'tarabih_recoverable':subscriber.tarabih_recoverable
                        }
                    )
                
                
    year = str(datetime.datetime.today().year)
    if 'year' in request.GET:
        year = request.GET['year']
    fees = SubscriptionFee.objects.filter(year=year)
    sum_of_fees = {
        'mosque'        : fees.aggregate(Sum('mosque_recovered'))['mosque_recovered__sum'],
        'graveyeard'    : fees.aggregate(Sum('graveyeard_recovered'))['graveyeard_recovered__sum'],
        'eidgah'        : fees.aggregate(Sum('eidgah_recovered'))['eidgah_recovered__sum'],
        'mustichal'     : fees.aggregate(Sum('mustichal_recovered'))['mustichal_recovered__sum'],
        'tarabih'       : fees.aggregate(Sum('tarabih_recovered'))['tarabih_recovered__sum'],
    }
    grand_total = 0
    for key, value in sum_of_fees.items():
        if value is not None:
            grand_total += value

    template = "Organization/subscription_fees.html"
    context = {
        'fees': fees, 
        'year':year, 
        'sum_of_fees':sum_of_fees,
        'grand_total':grand_total
        }
    return render(request, template, context)