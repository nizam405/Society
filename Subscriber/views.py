from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# from .serializers import SubscriberSerializer
from .models import Subscriber
from .forms import SubscriberForm

def SubscriberList(request):
    subscribers = Subscriber.objects.all()
    template = "Subscriber/subscriber_list.html"
    context = {'subscribers': subscribers}
    return render(request, template, context)

def ShowSubscriber(request, subscriber_id):
    subscriber = Subscriber.objects.get(id=subscriber_id)
    template = "Subscriber/view_subscriber.html"
    context = {'subscriber': subscriber}
    return render(request, template, context)

def CreateSubscriber(request):
    form = SubscriberForm()
    template = "Subscriber/create_subscriber.html"
    context = {'form': form}
    return render(request, template, context)

# class SubscriberView(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Subscriber.objects.all()
#         serializer = SubscriberSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = SubscriberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# def SubscribersView(request):
#     template = ""
#     context = ""
#     return render(request, template, context=context)