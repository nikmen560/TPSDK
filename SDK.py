import sqlite3
from customer import Customer

def cursor():
	return sqlite3.connect('data.db').cursor()


def add_customer(customer):
	c = cursor()

	with c.connection:
		c.execute('INSERT INTO customers VALUES (?, ?, ?)', (customer.name, customer.surname, customer.address))
		
	return c.lastrowid

	