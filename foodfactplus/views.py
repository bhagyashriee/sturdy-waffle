from django.http import JsonResponse
from .usda import get_nutrition_info
from django.shortcuts import render

from .forms import RecipeForm




def get_nutrition(request):
    food_name = request.GET.get('food_name')

    if not food_name:
        return render(request, 'foodfactplus/search_food.html', {'error': 'Food name is required.'})

  
    nutrition = get_nutrition_info(food_name)

    
    if not nutrition:
        return render(request, 'foodfactplus/search_food.html', {'error': 'No nutrition info found for this food.'})

    return render(request, 'foodfactplus/nutrition.html', {'nutrition': nutrition})

def recipe_view(request):
    total_nutrition = {
        'energy': 0,
        'protein': 0,
        'fat': 0,
        'carbohydrates': 0,
    }

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
           
            food_items = form.cleaned_data['food_items'].split(',')
            
          
            for item in food_items:
                item = item.strip()  
                info = get_nutrition_info(item) 
                if info: 
                    total_nutrition['energy'] += info.get('energy', 0)
                    total_nutrition['protein'] += info.get('protein', 0)
                    total_nutrition['fat'] += info.get('fat', 0)
                    total_nutrition['carbohydrates'] += info.get('carbohydrates', 0)
                else:
                    print(f"No nutrition info found for: {item}")

         
            return render(request, 'foodfactplus/recipe.html', {'form': form, 'nutrition': total_nutrition})

    else:
        form = RecipeForm()  

    return render(request, 'foodfactplus/recipe.html', {'form': form})
