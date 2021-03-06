from django.urls import path

from .views import SubscriberList, ShowSubscriber, CreateSubscriber

urlpatterns = [
    path("", SubscriberList, name='subscriber_list'),
    path("add/", CreateSubscriber, name="create_subscriber"),
    path("<subscriber_id>/", ShowSubscriber, name='show_subscriber')
]