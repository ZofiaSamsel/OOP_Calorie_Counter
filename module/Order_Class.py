from typing import List
from module.functions_calorie_counter import calorie_counter_advanced_data, costs_counter_advanced_data
from datetime import datetime



class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (date): The date and time of the order. e.g., "1-Jan-2022"

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
    counter: int = 0

    def __init__(
            self,
            items: "List",
            date=None
    ):
        Order.counter += 1
        self.order_id: str = f"order--{self.counter}"
        self._calories = None
        self._price = None
        self.order_accepted = None
        self.order_refused_reason = None
        self.items = items
        self.date = datetime.strptime(
            date, "%d-%b-%Y").strftime("%Y-%m-%d") if date else datetime.today().strftime("%Y-%m-%d")

        self.calories
        self.price


    @property
    def calories(self):
        if self._calories is None:
            try:
                self._calories = calorie_counter_advanced_data(self.items)
                self.order_accepted = True
            except Exception as e:
                self.order_refused_reason = str(e)
                self.order_accepted = False
        return self._calories

    @property
    def price(self):
        if self._price is None and self._calories is not None:
            self._price = costs_counter_advanced_data(self.items)
        return self._price
#