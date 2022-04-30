"""
Use Places API to access locations using longitude and latitude
Reference: https://developer.here.com/documentation/places/topics_api/resource-explore.html
Categories Reference: https://developer.here.com/documentation/places/topics_api/resource-explore.html
"""
import os

PLACES_API_BASE_URL = 'https://places.ls.hereapi.com/places/v1/discover/explore?'
PLACES_API_APP_KEY = "Tn07i1u1JUQ5rkSS1ikVb7KBaOLTFGgZc-Oy7y--4kM" #os.environ.get("PLACES_API_APP_KEY", None)

PLACES_SEARCH_API_URL = PLACES_API_BASE_URL + 'at={latitude},{longitude}&cat={places_query}'

if PLACES_API_APP_KEY:
    PLACES_SEARCH_API_URL += '&apiKey=' + PLACES_API_APP_KEY
