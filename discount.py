class Discount:
    def __init__(self, percent, product_id, customer_id, date, discount_id=None):
        self.percent = percent
        self.product_id = product_id
        self.customer_id = customer_id
        self.date = date

    def __str__(self):
        return self.product_id + ' ' + self.customer_id + ' ' + self.percent
