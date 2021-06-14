import sqlite3
from customer import Customer
from product import Product


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
        c.execute('SELECT rowid, * FROM customers')
        records = c.fetchall()

        for row in records:
            print(f' {row[0]} {row[1]} {row[2]}')

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
# 	discount_id INTEGER PRIMARY KEY,
# 	percent INTEGER NOT NULL,
# 	product_id INTEGER NOT NULL,
# 	customer_id INTEGER NOT NULL)
#         ''')

# def create_table():
#     c = cursor()
#     with c.connection:
#         c.execute('''
#         CREATE TABLE products (
# 	name TEXT NOT NULL,
# 	price REAL NOT NULL,
# 	product_id INTEGER PRIMARY KEY)
#         ''')
#     c.connection.close()

##################################################### PRODUCTS
def drop_table():
    c = cursor()
    with c.connection:
        c.execute('DROP TABLE products')
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
        c.execute('''UPDATE products SET name=?, price=? WHERE name=? AND price=?''', (new_name, new_price, product.name, product.price))
    product = get_product_by_name(new_name)
    c.connection.close()
    return product


def create_discount(discount):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO discounts VALUES (?, ?, ?, ?)',
                  (discount.discount_id, discount.percent, discount.product_id, discount.customer_id))
    c.connection.close()
    return c.lastrowid
