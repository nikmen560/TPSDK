import sqlite3
from customer import Customer

def cursor():
	return sqlite3.connect('data.db').cursor()


def add_customer(customer):
	c = cursor()

	with c.connection:
		c.execute('INSERT INTO customers VALUES (?, ?, ?)', (customer.name, customer.surname, customer.address))
		
	return c.lastrowid

def get_customers():
	c = cursor()
	customers = []
	with c.connection:
		c.execute('SELECT * FROM customers')
		records = c.fetchall()
		for row in records:
			print(f'{row[0]} {row[1]} {row[2]}')
		#	print('name: ', row[0])
		#	print('surname: ', row[1])
		#	print('address: ', row[2])
		#	print('\n')



