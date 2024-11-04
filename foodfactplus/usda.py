import requests
import os
from dotenv import load_dotenv

load_dotenv()
def get_nutrition_info(food_name):
    # Replace YOUR_API_KEY with your actual API key
    api_key = os.getenv('api_key')  # Load the API key from environment variables

    if api_key is None:
        raise ValueError("api_key is not set in environment variables")
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={food_name}&nutrients=*'
    response = requests.get(url)
    data = response.json()

    # Check if the API returned any results
    if data['totalHits'] == 0:
        return None

    # Get the first result from the API response
    nutrition={}
    food = data['foods'][0]
    for nutrient in food['foodNutrients']:
        nutrition[nutrient['nutrientName']] = nutrient['value']

    return nutrition