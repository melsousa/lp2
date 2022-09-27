from orders.Subject import Subject
from orders.OrderCreated import OrderCreated

class UpdateQuantityProductWhenOrderIsCreated(Subject):
    def notify(event:OrderCreated):
        print("When", event.instant())
        
        # event.payload().items().forEach
        