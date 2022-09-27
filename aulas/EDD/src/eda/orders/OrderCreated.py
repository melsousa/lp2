from datetime import datetime

from Order import Order


class OrderCreatred:
    instant: datetime

    def __init__(self, palyload: Order):
        self.palyload = palyload
        self.instant = datetime.now()

    def instant(self):
        return self.instant

    def payload(self):
        return self.palyload
