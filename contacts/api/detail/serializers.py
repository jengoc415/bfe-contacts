from rest_framework import serializers

from .models import Detail


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detail
        fields = ('id', 'name', 'phone_number', 'email',
                  'birthday', 'address')
