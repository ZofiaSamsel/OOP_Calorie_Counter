
import json

# Read data from json files
file_combos = open("data/json_files/combos.json")
combos_advanced = json.load(file_combos)
file_combos.close()

file_meals = open("data/json_files/meals.json")
menus_advanced = json.load(file_meals)
file_meals.close()

# Modify the list of dict to one dict of meals
combos_advanced = {combo["id"]: combo for combo in combos_advanced["combos"]}
menus_advanced = {meal["id"]: meal for meal in menus_advanced["meals"]}
