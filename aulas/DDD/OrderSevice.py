from gc import callbacks
from ddd_domain_events import DomainEvents, DomainEventCallable
from typing import List

from OrderItem import OrderItem
from OrderEvent import OrderEvent
from Order import Order

class OrderSevice:
    @classmethod
    def create_order(cls, order_items: List[OrderItem]) -> Order:
        with DomainEvents() as domain_events:
            callbacks = [
                DomainEventCallable(OrderEvent.HIGH_VOLUME_PRICE, cls.notify_top_management),
                DomainEventCallable(OrderEvent.HIGH_VOLUME_PRICE, cls.notify_sales_team),
                DomainEventCallable(OrderEvent.HIGH_QUANTITY, cls.notify_inventory_team)]
            
            for callback in callbacks:
                domain_events.register_event(callback)
            
            order = Order()
            
            order.add_order_item(order_items)
            
            return order
    
    @staticmethod
    def notify_sales_team(order: Order) -> None:
        """A callback for notifying the sales team about the important order"""

    @staticmethod
    def notify_top_management(order: Order) -> None:
        """A callback for notifying the top management about the important order"""

    @staticmethod
    def notify_inventory_team(order: Order) -> None:
        """A callback for notifying the inventory team required quantities"""