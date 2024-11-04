import os
from dotenv import load_dotenv
import requests


load_dotenv()

def get_nutrition_info(food_name):
    #
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')

    if api_key is None:
        raise ValueError("API_KEY is not set in environment variables")
    if api_url is None:
        raise ValueError("API_URL is not set in environment variables")

   s
    url = f'{api_url}?api_key={api_key}&query={food_name}&nutrients=*'
    response = requests.get(url)
    data = response.json()

   
    if data['totalHits'] == 0:
        return None

  
    nutrition = {}
    food = data['foods'][0]
    for nutrient in food['foodNutrients']:
        nutrition[nutrient['nutrientName']] = nutrient['value']

    return nutrition
