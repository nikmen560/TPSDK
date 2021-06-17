import sqlite3
import datetime
from customer import Customer
from product import Product


def cursor():
    return sqlite3.connect('data.db').cursor()


def add_customer(customer):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO customers VALUES (?, ?, ?, NULL)', (customer.name, customer.surname, customer.address))
    c.connection.close()
    return c.lastrowid


def get_customers():
    c = cursor()
    customers = []

    with c.connection:
        c.execute('SELECT * FROM customers')
        records = c.fetchall()

        for row in records:
            print(f'#{row[3]} {row[0]} {row[1]} город: {row[2]}')

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


# def create_table():
#     c = cursor()
#     with c.connection:
#         c.execute('''
#         CREATE TABLE discounts (
# 	percent INTEGER NOT NULL,
# 	product_id INTEGER NOT NULL,
# 	customer_id INTEGER NOT NULL,
#   date
# 	discount_id INTEGER PRIMARY KEY,
# 	)
#         ''')

def create_table():
    c = cursor()
    with c.connection:
        c.execute('''
        CREATE TABLE discounts (
	percent INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	customer_id INTEGER NOT NULL,
	date timestamp,
	 discount_id INTEGER PRIMARY KEY)
        ''')
    c.connection.close()


##################################################### PRODUCTS
def drop_table():
    c = cursor()
    with c.connection:
        c.execute('DROP TABLE customers')
    c.connection.close()


def add_product(product):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO products VALUES (?,?,NULL)', (product.name, product.price))
    c.connection.close()
    return c.lastrowid


def get_products():
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM products')
        records = c.fetchall()

        for row in records:
            print(f'#{row[2]} {row[0]} {row[1]} руб')

    c.connection.close()


def get_product_by_name(name):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM products WHERE name=?', (name,))
    data = c.fetchone()

    if not data:
        return None

    return Product(data[0], data[1])


def update_product(product, new_name, new_price):
    c = cursor()
    with c.connection:
        c.execute('''UPDATE products SET name=?, price=? WHERE name=? AND price=?''',
                  (new_name, new_price, product.name, product.price))
    product = get_product_by_name(new_name)
    c.connection.close()
    return product


def add_discount(discount):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO discounts VALUES (?, ?, ?, ?, NULL)',
                  (discount.percent, discount.product_id, discount.customer_id, discount.date))
    c.connection.close()


def get_customer_by_id(id):
    c = cursor()

    with c.connection:
        c.execute('SELECT name, surname, address FROM customers WHERE customer_id=?', (id,))
        data = c.fetchone()

        if not data:
            return None

        return Customer(data[0], data[1], data[2])


def get_product_by_id(id):
    c = cursor()

    with c.connection:
        c.execute('SELECT name, price FROM products WHERE product_id=?', (id,))
        data = c.fetchone()

        if not data:
            return None

        return Product(data[0], data[1])


def get_discounts():
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM discounts')
        records = c.fetchall()

        for row in records:
            customer = get_customer_by_id(row[2])
            product = get_product_by_id(row[1])
            print(f'#{row[4]} товар: {product} скидка: {row[0]}% для покупателя: {customer} дата начала: {row[3]}')

    c.connection.close()


def get_discount_by_customer_id(customer_id):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM discounts WHERE customer_id=? ORDER BY date ASC', (customer_id,))
        # c.execute('SELECT * FROM discounts ORDER by date(date) DESC')
        records = c.fetchall()

        for row in records:
            customer = get_customer_by_id(row[2])
            product = get_product_by_id(row[1])
            print(f'товар: {product} скидка: {row[0]}% начало действия скидки: {row[3]}')

    c.connection.close()


def get_discounts_by_interval(customer_id, date_start, date_end):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM discounts WHERE customer_id=? AND date BETWEEN ? AND ?',
                  (customer_id, date_start, date_end))
        records = c.fetchall()

        for row in records:
            customer = get_customer_by_id(row[2])
            product = get_product_by_id(row[1])
            print(f'товар: {product} скидка: {row[0]}% начало действия скидки: {row[3]}')

    c.connection.close()


def get_discounts_average(id, column_name):
    c = cursor()
    with c.connection:
        c.execute(f'SELECT *, AVG(percent) FROM discounts WHERE {column_name}=?', id, )
        records = c.fetchall()

        for row in records:
            if row[0] is not None:
                customer = get_customer_by_id(row[2])
                print(f'покупатель: {customer.name} {customer.surname} г. {customer.address} средняя скидка на товары: {row[5]}%')

    c.connection.close()


def get_ids(name_id, table_name):
    c = cursor()
    customers_id = []
    with c.connection:
        c.execute(f'SELECT {name_id} FROM {table_name}')
        records = c.fetchall()
    return records


def get_average_by_product(id, column_name):
    c = cursor()
    customer_length = get_ids('customer_id', 'customers')
    records = []
    with c.connection:
        for customer in customer_length:
            c.execute(f'SELECT customer_id, AVG(percent) FROM discounts WHERE product_id=? AND customer_id =?', (id, customer[0]))
            records.append(c.fetchall())
        for row in records:
            for rowing in row:
                if rowing[0] is not None:
                    customer = get_customer_by_id(rowing[0])
                    # product = get_product_by_id(row[1])
                    print(f'{customer.name} {customer.surname} г. {customer.address} средняя скидка: {rowing[1]}%')
                    # print(f'{customer.name} {rowing[0]}')

    c.connection.close()