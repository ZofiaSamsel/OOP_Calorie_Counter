#create the exception for the situation when the meals' calories is greater then 2000
class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f'Too many calories: {calories}; maximum is 2000.'
        super().__init__(self.message)

#create the exception for the situation when the meal in the order is out of the dict.
class MealOutOfTheMenu(Exception):
    def __init__(self, meal):
        self.message = f'The meal "{meal}" is not in the menu.'
        super().__init__(self.message)
