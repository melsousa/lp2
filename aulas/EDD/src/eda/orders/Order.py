import stream
from os import stat
from typing import List

from ProductItem import ProductItem
from products.Product import Product 
from Address import Address
from Status import Status

class Order:
    items:List[ProductItem] = []
    
    def __init__(self, id, items, customerId, status:Status, address:Address):
        self.id = id
        self.items = items
        self.customerId = customerId
        self.status = status
        self.address = address
        
    # def total(self, items):
    #     return items(map(item -> item.price))
    
    def id(self):
        return self.id
    
    def items(self):
        return self.items #retornar uma lista imodificavel
    
    def customerId(self):
        return self.customerId
    
    def status(self):
        return self.status
    
    def address(self):
        return self.address
        
        