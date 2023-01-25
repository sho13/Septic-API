from django.shortcuts import render
from django.http import HttpResponse
import json

from housecanary.services.housecanary_service import (
    HouseCanaryService,
)

RECOGNIZED_RESPONSES = [
    'municipal',
    'storm',
    'septic',
    'yes',
    'none'
]

def get_have_septic(request):
    address = request.GET.get('address', None)
    zipcode = request.GET.get('zipcode', None)

    house_canary_response = HouseCanaryService.get_house_canary(address=address, zipcode=zipcode)

    sewer = house_canary_response['property/details']['result']['property']['sewer']

    if sewer == 'septic':
        result = True
    else:
        result = False
    
    return HttpResponse(json.dumps({"validated": result}))