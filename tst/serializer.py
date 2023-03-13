from rest_framework import serializers
from .models import Tst


class TstSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tst
        fields = ('id', 'url', 'name', 'surname', 'email')

