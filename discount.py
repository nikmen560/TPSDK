class Discount:
    def __init__(self, discount_id, percent, product_id, customer_id):
        self.discount_id = discount_id
        self.percent = percent
        self.product_id = product_id
        self.customer_id = customer_id

    def __str__(self):
        return self.product_id + ' ' + self.customer_id + ' ' + self.percent
