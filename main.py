# Main Program

class Meal:
    def __init__(self, name, calories, ingredients):
        self.name = name
        self.calories = calories
        self.ingredients = ingredients
        
def add_meal(meals):
    name = input("Enter meal name: ")
    calories = int(input("Enter calories: "))
    ingredients = input("Enter ingredients (comma separated): ").split(',')
    meals.append(Meal(name, calories, [ingredient.strip() for ingredient in ingredients]))

def delete_meal(meals):
    name = input("Which meal do you want to delete")
    for m in meals:
        if m.name == name:
            meals.remove(m)
            print(f"{name} has been deleted.")
            return
    print(f"{name} not found.")

def main():
    running = True
    meals = []
    while(running):
        print("What command would you like to run? Enter number for command\n")
        commands = ["Exit ","Add meal", "Delete Meal"]
        for index, command in enumerate(commands):
            print(f"{index} - {command}\n")
        user_command = input()
        match user_command:
            case "0":
                running = False
            case "1":
                add_meal(meals)
            case "2":
                delete_meal(meals)
            case _:
                print("Invalid Command. Please enter a valid value\n")


if __name__ == "__main__":
        main()
