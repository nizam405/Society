from django.urls import path

from .views import SubscriberList, ShowSubscriber

urlpatterns = [
    path("", SubscriberList, name='subscriber_list'),
    path("<subscriber_id>/", ShowSubscriber, name='show_subscriber')
]