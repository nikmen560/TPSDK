class Customer:
	def __init__(self, name, surname, address, customer_id=None):
		self.name = name
		self.surname = surname
		self.address = address

	def __str__(self):
		return self.name + ' ' + self.surname + ' ' + self.address
