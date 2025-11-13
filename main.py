# Main Program

class Meal:
    def __init__(self, name, calories, ingredients):
        self.name = name
        self.calories = calories
        self.ingredients = ingredients
        
def add_meal(meal):
    name = input("Enter meal name: ")
    calories = int(input("Enter calories: "))
    ingredients = input("Enter ingredients (comma separated): ").split(',')
    meal.append(Meal(name, calories, [ingredient.strip() for ingredient in ingredients]))