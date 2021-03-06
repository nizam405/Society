import datetime
from django.shortcuts import render
from django.db.models import Sum
from .models import SubscriptionFee, Revenue, Expense

# Create your views here.
def SubscriptionFees(request):
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