from django.urls import path

from .views import   SubscriptionFees

urlpatterns = [
    path("subscription-fees/", SubscriptionFees, name='subscription_fees'),
    #path("<subscriber_id>/", ShowSubscriber, name='show_subscriber')
]