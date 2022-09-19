from ddd_domain_events import DomainEvents
from typing import List
from OrderItem import OrderItem
from OrderEvent import OrderEvent

class Order:
    HIGH_VOLUME_PRICE = 1_000_000
    HIGH_QUANTITY = 10_000

    def __init__(self):
        self.order_items = []

    @property
    def order_items(self):
        for order_item in self.order_items:
            yield order_item

    def add_order_item(self, order_items: List[OrderItem]) -> None:
        total_price = 0
        total_quantity = 0

        for order_item in order_items:
            total_price += (order_item.price * order_item.quantity)
            total_quantity += order_item.quantity
            self.order_items.append(order_item)

        if total_price >= self.HIGH_VOLUME_PRICE:
            DomainEvents.raise_event(OrderEvent.HIGH_VOLUME_PRICE, order=self)
        
        if total_quantity >= self.HIGH_QUANTITY:
            DomainEvents.raise_event(OrderEvent.HIGH_QUANTITY, order=self)