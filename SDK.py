import sqlite3
from customer import Customer


def cursor():
    return sqlite3.connect('data.db').cursor()


def add_customer(customer):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO customers VALUES (?, ?, ?)', (customer.name, customer.surname, customer.address))
    c.connection.close()
    return c.lastrowid


def get_customers():
    c = cursor()
    customers = []

    with c.connection:
        c.execute('SELECT * FROM customers')
        records = c.fetchall()

        for row in records:
            print(f'{row[0]} {row[1]} {row[2]}')

    c.connection.close()


def get_customer_by_name(name):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM customers WHERE name=?', (name,))
    data = c.fetchone()

    if not data:
        return None

    return Customer(data[0], data[1], data[2])


def update_customer(customer, new_name, new_surname, new_address):
    c = cursor()
    with c.connection:
        c.execute('''UPDATE customers SET name=?, surname=?,
		  		 address=? WHERE name=? AND surname=? AND address=?''',
                  (new_name, new_surname, new_address, customer.name, customer.surname, customer.address))
    customer = get_customer_by_name(new_name)
    c.connection.close()
    return customer

