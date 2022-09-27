from pyrecord import Record

class ProductItem:
    ProductItem = Record("productId", "name", "price", "quantity")