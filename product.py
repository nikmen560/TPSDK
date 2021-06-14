class Product:
    def __init__(self, name, product_id):
        self.name = name
        self.product_id = product_id

    def __str__(self):
        return self.product_id + ' ' + self.name
