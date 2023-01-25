from django.conf import settings
import json
import requests

HOUSECANARY_API_KEY = settings.HOUSECANARY_API_KEY
HOUSECANARY_BASE_URL= settings.HOUSECANARY_BASE_URL
HOUSECANARY_DEV_ENV = settings.HOUSECANARY_DEV_ENV

RECOGNIZED_FALSE_RESPONSES = {
  'municipal',
  'storm',
  'septic',
  'none',
  'yes'
}
SEPTIC = 'septic'

class HouseCanaryService:
    @classmethod
    def get_house_canary(self, address=None, zipcode=None):
        # Use mock data if HOUSECANARY_DEV_ENV is true
        if HOUSECANARY_DEV_ENV == 'true':
            with open('mock_property.json') as json_file:
                property_response = json.load(json_file)
                return property_response
        
        if HOUSECANARY_API_KEY and HOUSECANARY_BASE_URL and HOUSECANARY_BASE_URL != 'MOCK':
            response = requests.get(f"{HOUSECANARY_BASE_URL}/property/details?address={address}&zipcode={zipcode}")
            property_response = response.json()

            return property_response
        
