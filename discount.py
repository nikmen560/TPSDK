class Discount:
    def __init__(self, percent, customer_id, product_id, discount_id):
        self.percent = percent
        self.customer_id = customer_id
        self.product_id = product_id
        self.discount_id = discount_id

    def __str__(self):
        return self.product_id + ' ' + self.customer_id + ' ' + self.percent
