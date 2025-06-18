from rest_framework import generics
from .models import Event, Sermon, Donation, ContactMessage
from .Serializer import EventSerializer, SermonSerializer, DonationSerializer, ContactMessageSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer

class SermonListCreateView(generics.ListCreateAPIView):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer

class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all().order_by('-created_at')
    serializer_class = DonationSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
