from orders.Subject import Subject
from orders.OrderCreated import OrderCreated

class SendProductWhenOrderIsCreated(Subject):
    def notify(event:OrderCreated):
        print("When", event.instant())
        print("SEND PRODUCT")
    