class Product:
    def __init__(self, name, price, product_id=None):
        self.name = name
        self.price = price
        self.product_id = product_id

    def __str__(self):
        return  str(self.product_id) + ' ' + self.name + 'price ' + str(self.price)
