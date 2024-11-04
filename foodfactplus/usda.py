import os
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file
load_dotenv()

def get_nutrition_info(food_name):
    # Load the API key and base URL from environment variables
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')

    if api_key is None:
        raise ValueError("API_KEY is not set in environment variables")
    if api_url is None:
        raise ValueError("API_URL is not set in environment variables")

    # Construct the full URL using the base URL and the query parameters
    url = f'{api_url}?api_key={api_key}&query={food_name}&nutrients=*'
    response = requests.get(url)
    data = response.json()

    # Check if the API returned any results
    if data['totalHits'] == 0:
        return None

    # Get the first result from the API response
    nutrition = {}
    food = data['foods'][0]
    for nutrient in food['foodNutrients']:
        nutrition[nutrient['nutrientName']] = nutrient['value']

    return nutrition
