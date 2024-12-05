import json

def json_file(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None

def find_market_for_recipe(recipe, available_products):
    recipe_ingredients = set(recipe)
    market_ingredients = {market: set(products) for market, products in available_products.items()}

    market_needed = set()
    covered_ingredients = set()

    for market, products in sorted(market_ingredients.items(), key=lambda x: len(x[1]), reverse=True):
        if not recipe_ingredients.issubset(covered_ingredients):
            intersection = recipe_ingredients - covered_ingredients
            if intersection & products:
                market_needed.add(market)
                for product in products:
                    covered_ingredients.add(product)
    if not recipe_ingredients.issubset(covered_ingredients):
        missing_ingredients = recipe_ingredients - covered_ingredients
        return None, missing_ingredients
    
    return market_needed, None

def main():
    recipes_file = 'recipes.json'
    markets_file = 'markets.json'

    recipes = json_file(recipes_file)
    available_products = json_file(markets_file)

    if recipes is None or available_products is None:
        return
    dish_name = input("Enter the name of the dish you want to cook: ").strip()
    if dish_name not in recipes:
        print(f"Sorry, the recipe for '{dish_name}' is not available.")
        return
    recipe = recipes[dish_name]["ingredients"]
    markets, missing_ingredients = find_market_for_recipe(recipe, available_products)

    if missing_ingredients:
        print(f"Sorry, the dish '{dish_name}' cannot be prepared in this city. Missing ingredients: \n{(missing_ingredients)}.")
    else:
        print(f"To prepare '{dish_name}', you need to visit the following markets(s): \n{(markets)}.")

if __name__ == "__main__":
    main()
