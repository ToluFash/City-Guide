from datetime import timedelta

import requests
import requests_cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.commonresponses import DOWNSTREAM_ERROR_RESPONSE
from api.modules.food.constants import FOOD_API_REQUEST_HEADERS, GET_ALL_RESTAURANTS_API_URL, GET_RESTAURANT_API_URL
from api.modules.food.food_response import FoodResponse, FoodDetailedResponse
from api.modules.hyperlocal.constants import PLACES_SEARCH_API_URL
from api.modules.hyperlocal.hyperlocal_response import HyperLocalResponse

hour_difference = timedelta(days=1)
requests_cache.install_cache(expire_after=hour_difference)


@api_view(['GET'])
def get_all_restaurants(request, latitude, longitude):
    """
    Returns restaurant details forecast for given city using coordinates
    :param request:
    :param latitude:
    :param longitude:
    :return: 503 if Here API fails
    :return: 200 successful
    """
    response = []
    try:
        url = PLACES_SEARCH_API_URL.format(latitude=latitude, longitude=longitude, places_query="eat-drink")
        api_response = requests.get(url)
        api_response_json = api_response.json()
        if not api_response.ok:
            error_message = api_response_json['message']
            return Response(error_message, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        suggestions = api_response_json['results']['items']
        id_ = 0
        for restaurant_obj in suggestions:
            response_obj = FoodResponse(id=id_,
                                        name=restaurant_obj['title'],
                                        url=restaurant_obj['href'],
                                        latitude=restaurant_obj['position'][0],
                                        longitude=restaurant_obj['position'][1],
                                        avg2=0,
                                        currency=0,
                                        image=restaurant_obj['icon'],
                                        rating=restaurant_obj['averageRating'],
                                        votes=0,
                                        address="N/A")
            response.append(response_obj.to_json())
            id_ += 1
    except Exception as ex:
        print(ex)
        return DOWNSTREAM_ERROR_RESPONSE

    return Response(response)


@api_view(['GET'])
def get_restaurant(request, restaurant_id):
    """
    Returns restaurant details for a given restaurant id
    :param request:
    :param restaurant_id:
    :return: 503 if Zomato API fails
    :return: 200 successful
    """
    try:
        url = GET_RESTAURANT_API_URL.format(restaurant_id)
        api_response = requests.get(url, headers=FOOD_API_REQUEST_HEADERS)
        api_response_json = api_response.json()
        if not api_response.ok:
            error_message = api_response_json['message']
            return Response(error_message, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        response = FoodDetailedResponse(
            id=api_response_json['id'],
            name=api_response_json['name'],
            url=api_response_json['url'],
            address=api_response_json['location']['address'],
            longitude=api_response_json['location']['longitude'],
            latitude=api_response_json['location']['latitude'],
            avg2=api_response_json['average_cost_for_two'],
            price_range=api_response_json['price_range'],
            currency=api_response_json['currency'],
            img=api_response_json['featured_image'],
            agg_rating=api_response_json['user_rating']['aggregate_rating'],
            votes=api_response_json['user_rating']['votes'],
            deliver=api_response_json['has_online_delivery'],
            booking=api_response_json['has_table_booking'],
            cuisines=api_response_json['cuisines']
        ).to_json()
    except Exception:
        return DOWNSTREAM_ERROR_RESPONSE

    return Response(response)
