class Customer:
	def __init__(self, name, surname, address, customer_id=None):
		self.name = name
		self.surname = surname
		self.address = address
		self.customer_id = customer_id

	def __str__(self):
		return str(self.customer_id) + ' ' + self.name + ' ' + self.surname + ' ' + self.address
