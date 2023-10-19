#import inittest
from unittest import TestCase

#import datetime
from datetime import datetime

#import exceptions
from module.exception import MealOutOfTheMenu, MealTooBigError

#import calorie counter functions
from module.functions_calorie_counter import calorie_counter_advanced_data, costs_counter_advanced_data

#import Order class
from module.Order_Class import Order

#Order class tests
class OrderClassTestCase(TestCase):
    #id
    def test_order_id_counter_change(self):
        order_1 = Order(['meal-1'], date = "1-Jan-2022").order_id
        order_2 = Order(['combo-3']).order_id
        self.assertEqual(order_1, 'order--1', f"Expected 'order--1', got {order_1}")
        self.assertEqual(order_2, 'order--2', f"Expected 'order--2', got {order_2}")
    
    #date
    def test_order_with_the_predefine_date(self):
        order = Order(['meal-1', 'meal-2'], date="1-Jan-2022")
        self.assertEqual(order.date, "2022-01-01")
    
    def test_order_without_the_predefine_date(self):
        order = Order(['meal-1', 'meal-2'])
        self.assertEqual(order.date, datetime.today().strftime("%Y-%m-%d"))
    
    #calories of meals and combos
    def test_order_calories_calouter_with_meals(self):
        order = Order(['meal-1']).calories
        self.assertEqual(order, 600, f"Expected 600, got {order}")
        
    def test_order_calories_calouter_with_combos(self):
        result = Order(['combo-2']).calories
        self.assertEqual(result, 700, f'expected 700, got {result}')

    def test_order_calories_calouter_with_meals_and_combos(self):
        result = Order(['meal-1','combo-2']).calories
        self.assertEqual(result, 1300, f'expected 1300, got {result}')

    #exception MealOutOfTheMenu
    def test_order_creation_exception_MealOutOfTheMeal(self):
        with self.assertRaises(MealOutOfTheMenu) as e:
            Order(['invalid-meal']).order_refused_reason
            self.assertEqual(e.exception.message, 'A meal "invalid-meal" is not in the menu', 
                             f'Wrong message; expected: A meal "invalid-meal" is not in the menu')

    #excpetion MealTooBigError
    def test_order_creation_exception_MealTooBigError(self):
        with self.assertRaises(MealTooBigError) as e:
            Order(['meal-1','combo-2','meal-4','combo-3']).order_refused_reason 
            self.assertEqual(e.exception.message, 'Too many calories: 2105', 
                             f'Wrong message; expected: Too many calories: 2105')
    
    #price of meals and combos
    def test_order_price_with_meals(self):
        result = Order(['meal-1']).price
        self.assertEqual(result, 5, f"Expected 5, got {result}")
        
    def test_order_price_with_combos(self):
        result = Order(['combo-1']).price
        self.assertEqual(result, 11, f'expected 11, got {result}')

    def test_order_price_with_meals_and_combos(self):
        result = Order(['combo-1', 'meal-1']).price
        self.assertEqual(result, 16, f'expected 16, got {result}')

    def test_order_price_when_MealTooBigError(self):
        result = Order(['combo-1', 'meal-1','combo-1', 'meal-1']).price
        self.assertEqual(result, None, f'expected None, got {result}')

    #order_accepted 
    def test_order_if_order_accepted_correct(self):
        result = Order(['combo-1', 'meal-1']).order_accepted
        self.assertEqual(result, True, f'expected True, got {result}')

    def test_order_if_order_accepted_incorrect(self):
        result = Order(['invalid-meal']).order_accepted
        self.assertEqual(result, False, f'expected False, got {result}')
