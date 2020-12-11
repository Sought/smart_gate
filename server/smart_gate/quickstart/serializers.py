from smart_gate.quickstart.models import Entry
from rest_framework import serializers

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['isEntry', 'time']
