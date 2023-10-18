class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f'Too many calories: {calories}'
        super().__init__(self.message)

class MealOutOfTheMenu(Exception):
    def __init__(self, meal):
        self.message = f'A meal "{meal}" is not in the menu'
        super().__init__(self.message)
