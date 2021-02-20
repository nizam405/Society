from django.test import TestCase
from models import Subscriber

# Create your tests here.
def suggest_serial_num():
    serials = Subscriber.objects.values_list('serial_num')
    num_of_serials = serials.count()
    last_serial = serials.last()[0]
    if last_serial == num_of_serials:
        return ""
    skipped_serials = []
    i = 0
    while i < last_serial:
        if i != serials[i][0]:
            skipped_serials.append(i+1)
            # i += 1
        i += 1
    txt = "Skipped serials are" + skipped_serials
    return txt

print(suggest_serial_num())