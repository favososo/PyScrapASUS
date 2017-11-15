from LTE.models import bands
from LTE.serializers import bandsSerializer

from rest_framework import viewsets
import requests
from django.http import HttpResponse
#from rest_framework.permissions import IsAuthenticated


# Create your views here.
class bandsViewSet(viewsets.ModelViewSet):
    queryset = bands.objects.all()
    serializer_class = bandsSerializer
#    permission_classes = (IsAuthenticated,)

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
