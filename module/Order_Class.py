from typing import List, Optional
import datetime
import random
import json

from module.functions_calorie_counter import calorie_counter_advanced_data, costs_counter_advanced_data


class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (date): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(
            self, 
            items: "List", 
            date: Optional[datetime.date] = None
            ):
        Order.counter += 1
        self.order_id: str = f"order--{self.counter}.{random.randrange(1,200)}"
        self._calories = None
        self._price = None
        self.order_accepted: bool = None
        self.order_refused_reason: str = None
        self.items = items
        self.date = date or datetime.date.today()

        try:
            self.calories
        except:
            pass
   
    @property
    def calories(self):
        if self._calories is None:
            self._calories = calorie_counter_advanced_data(self.items) #calculate calories
        return self._calories
    
    @property
    def price(self):
        _price = costs_counter_advanced_data(self.items)
        return _price
    




