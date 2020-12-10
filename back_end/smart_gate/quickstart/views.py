from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from smart_gate.quickstart.models import Entry
from smart_gate.quickstart.serializers import UserSerializer, GroupSerializer, EntrySerializer
from django.shortcuts import render    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('time')
    serializer_class = EntrySerializer

def index(request):
    
    all_items = Entry.objects.all()
    items_in = all_items.filter(isEntry=True)
    items_out = all_items.filter(isEntry=False)
    context = {
       'all_items' : all_items,
       'items_in' : items_in,
       'items_out' : items_out,
       'nb_in' : items_in.count(),
       'nb_out' : items_out.count(),
       'nb_still_in': items_in.count() - items_out.count(),
    }

    return render(request, 'index.html', context=context)
