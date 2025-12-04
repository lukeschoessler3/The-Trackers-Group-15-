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

def delete_meal(meals):
    name = input("Which meal do you want to delete")
    for m in meals:
        if m.name == name:
            meals.remove(m)
            print(f"{name} has been deleted.")
            return
    print(f"{name} not found.")

def edit_meal(meals):
    name = input("Which meal do you want to edit: ")
    for m in meals:
        if m.name == name:
            new_name = input("Enter new meal name: ")
            new_calories = int(input("Enter new calories: "))
            new_ingredients = input("Enter new ingredients (comma separated): ").split(',')
            m.name = new_name
            m.calories = new_calories
            m.ingredients = [ingredient.strip() for ingredient in new_ingredients]
            print(f"{name} has been updated.")
            return
    print(f"{name} not found.")