# import dictionaires of combos and calories
from data.read_data_files.data_easy_dict import combos, calories

#import the complex dictionaires related to combos and menus
from data.read_data_files.data_advanced_dict import menus_advanced, combos_advanced

#import exceptions
from module.exception import MealTooBigError, MealOutOfTheMenu

# BASIC FUNCTIONS

# function that count meals and combos together + exceptions
def total_calories_counter(meals):
   total_kcal = 0

   for meal in meals:  
      if calories.get(meal) is not None:
         # check if the meal is directly from the calories... 
         total_kcal += calories[meal]
      #...or if it is a combo  
      else:
         try:
            total_kcal += total_calories_counter(combos[meal]) 
         except KeyError: 
            raise MealOutOfTheMenu(meal)
         except:
            print("Other error occured.")
      if total_kcal >2000:
         raise MealTooBigError(total_kcal)
   return total_kcal



# ADVANCED DATA

# function that count calories from combos + meals - advanced - uses dictionaires
def calorie_counter_advanced_data(meals):
   total_kcal = 0
   for meal in meals:
   #checking menu
    if meal in menus_advanced.keys():
            total_kcal += menus_advanced[meal]['calories']
    else:
        try:
            #checking combos 
            total_kcal += calorie_counter_advanced_data(combos_advanced[meal]['meals'])
        except: 
         raise MealOutOfTheMenu(meal)
    if total_kcal > 2000:
        raise MealTooBigError(total_kcal)
   return total_kcal


# PRICES COUNTERS

#function that is calculating the total number of calories form the meals variable
# meals - list of names of dishes (list[strings])
def costs_counter_advanced_data(meals):
   total_cost = 0
   for meal in meals:
      try:
         #checking menu
         if meal in menus_advanced.keys():
            total_cost += menus_advanced[meal]['price']
         #checking combos 
         else:
            total_cost += combos_advanced[meal]['price']
      except: 
         raise MealOutOfTheMenu(meal)
   return total_cost


'''
#Other

# function that count calories from combos + meals - advanced - uses the lists od dictionaires 
def calorie_counter_advanced_2(*meals):
   total_kcal = 0
   for meal in meals[0]:
      try: 
         for menu in menus_advanced['meals']:
            if (menu['name'] == meal or menu['id'] == meal):
               total_kcal = total_kcal + menu['calories']   
         for combos_advanced_part in combos_advanced["combos"]:
            if combos_advanced_part['name'] == meal:
               total_kcal += calorie_counter_advanced_2(combos_advanced_part['meals'])   
         if total_kcal > 2000: 
            raise MealTooBigError(total_kcal)
      except KeyError:
         raise MealOutOfTheMenu(meal)
      except:
         print("Other error.")
   return total_kcal


#function that is calculating the total number of calories form the meals variable
# meals - list of names of dishes (list[strings])
def countMeals_v2(*meals):
   totalcost = 0
   for meal in meals:
      try:
         #if combo in combos
         #checking menu
         for menu in menus_advanced['meals']:
               if menu['name'] == meal:
                  totalcost += menu['price']
         #checking combos 
         for combos_part in combos_advanced['combos']:
               if combos_part['name'] == meal:
                  totalcost += combos_part['price']
      except: 
         raise MealOutOfTheMenu

   return totalcost
   
   '''
