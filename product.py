class Product:
    def __init__(self, name, price, product_id=None):
        self.name = name
        self.price = price

    def __str__(self):
        return f'"{self.name}" цена:  {str(self.price)} руб'
