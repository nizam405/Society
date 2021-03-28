import datetime
from django.shortcuts import render
from django.db.models import Sum
from .models import SubscriptionFee, Revenue, Expense
from Subscriber.models import Subscriber

# Create your views here.
def SubscriptionFees(request):
    # First ensure fees list of all active members till current year is created
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        if subscriber.active == True:
            sub_year = subscriber.subscription_date.year
            current_year = datetime.datetime.now().year
            # Create list for each year from subscription year to current year
            for year in range(sub_year,current_year+1):
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
        if request.GET['year'] != "":
            year = request.GET['year']
            fees = SubscriptionFee.objects.filter(year=year)
        else:
            year = ""
            fees = SubscriptionFee.objects.all()
    else:
        fees = SubscriptionFee.objects.filter(year=year)

    sum_of_fees = fees.aggregate(
        mosque = Sum('mosque_recovered'),
        graveyeard = Sum('graveyeard_recovered'),
        eidgah = Sum('eidgah_recovered'),
        mustichal = Sum('mustichal_recovered'),
        tarabih = Sum('tarabih_recovered')
    )
    # sum_of_recoverable = fees.aggregate(
    #     mosque_r = Sum('mosque_recoverable'),
    #     graveyeard_r = Sum('graveyeard_recoverable'),
    #     eidgah_r = Sum('eidgah_recoverable'),
    #     mustichal_r = Sum('mustichal_recoverable'),
    #     tarabih_r = Sum('tarabih_recoverable')
    # )
    # sum_of_fees returns a dictionary
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