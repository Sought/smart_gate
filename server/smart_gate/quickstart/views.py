from rest_framework import viewsets
from rest_framework import permissions
from smart_gate.quickstart.models import Entry
from smart_gate.quickstart.serializers import EntrySerializer
from django.shortcuts import render

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
