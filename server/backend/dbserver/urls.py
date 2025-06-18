from django.urls import path
from .views import (
    EventListCreateView, SermonListCreateView,
    DonationListCreateView, ContactMessageCreateView
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('sermons/', SermonListCreateView.as_view(), name='sermon-list'),
    path('donations/', DonationListCreateView.as_view(), name='donation-list'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-message'),
]
