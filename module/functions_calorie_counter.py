from module.exception import MealTooBigError, MealOutOfTheMenu
from data.read_data_files.data_advanced_dict import menus_advanced, combos_advanced
from data.read_data_files.data_easy_dict import combos, calories

# Basic data
def total_calories_counter(meals):
    '''
    function that count meals and combos together + exceptions
    '''
    total_kcal = 0

    for meal in meals:
        if calories.get(meal) is not None:
            # check if the meal is directly from the calories...
            total_kcal += calories[meal]
        # ...or if it is a combo
        else:
            try:
                total_kcal += total_calories_counter(combos[meal])
            except KeyError:
                raise MealOutOfTheMenu(meal)
            except:
                print("Other error occured.")
        if total_kcal > 2000:
            raise MealTooBigError(total_kcal)
    return total_kcal

# Advanced data
def calorie_counter_advanced_data(meals):
    '''
    function that count calories from combos + meals - advanced - uses dictionaires
    '''
    total_kcal = 0
    for meal in meals:
        # checking menu
        if meal in menus_advanced.keys():
            total_kcal += menus_advanced[meal]['calories']
        else:
            try:
                # checking combos
                total_kcal += calorie_counter_advanced_data(
                    combos_advanced[meal]['meals'])
            except:
                raise MealOutOfTheMenu(meal)
        if total_kcal > 2000:
            raise MealTooBigError(total_kcal)
    return total_kcal


# Price counter
def costs_counter_advanced_data(meals):
    '''
    function that is calculating the total number of calories form the meals variable
    meals - list of names of dishes (list[strings])
    '''
    total_cost = 0
    for meal in meals:
        try:
            # checking menu
            if meal in menus_advanced.keys():
                total_cost += menus_advanced[meal]['price']
            # checking combos
            else:
                total_cost += combos_advanced[meal]['price']
        except:
            raise MealOutOfTheMenu(meal)
    return total_cost

#
