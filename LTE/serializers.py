from django.utils.timezone import now
from rest_framework import serializers
from LTE.models import bands


class bandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = bands
        fields = '__all__'
        #fields = ('id', 'title', 'text', 'created_date', 'published_date', 'author_id')