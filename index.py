from customer import Customer
from product import Product
from discount import Discount
from datetime import datetime
import SDK


def convert_str_to_date(str_date):
    d = datetime.strptime(str_date, '%d/%m/%y')
    return d.date()


while True:
    print('''
    1. информация о покупателях
    2. скидки
    3. товары
    4. средний процент скидки у покупателей
    
    0. завершить работу
    ''')
    user_input = int(input())

    if user_input == 1:
        while True:
            SDK.get_customers()

            print('''
1. изменить покупателя
2. добавить покупателя
            
0. выход
            ''')

            user_input = int(input())

            if user_input == 1:
                while True:
                    SDK.get_customers()
                    customer_name = input('введите имя покупателя \n')
                    customer_obj = SDK.get_customer_by_name(customer_name)

                    user_input = int(input('изменить покупателя? \n 1. да \n 2. нет \n'))

                    if user_input == 1:
                        customer_new_name = input('введите новое имя: \n')
                        customer_new_surname = input('введите новую фамилию: \n')
                        customer_new_address = input('введите новый адрес: \n')
                        SDK.update_customer(customer_obj, customer_new_name, customer_new_surname,
                                            customer_new_address)
                        break
                    elif user_input == 2:
                        break

            elif user_input == 2:
                customer_name = input('введите имя: \n')
                customer_surname = input('введите фамилию: \n')
                customer_address = input('введите адрес: \n')
                customer = Customer(customer_name, customer_surname, customer_address)
                SDK.add_customer(customer)

            else:
                break

    elif user_input == 2:
        while True:

            print('''
1. создать новую скидку
2. показать список скидок в хронологическом порядке
3. список скидок покупателя за определнный интервал дат
4.
0. выход
                    ''')

            user_input = int(input())
            if user_input == 1:
                print('create new discount')
                percent = int(input('введите процент скидки \n '))
                SDK.get_products()
                product_id = int(input('выберите товар к которому будет применена скидка \n'))
                SDK.get_customers()
                customer_id = int(input('выберите для кого будет применяться скидка ?\n '))
                date = str(input('введите дату в формате dd/mm/yy'))
                date = convert_str_to_date(date)

                discount = Discount(percent, product_id, customer_id, date)
                SDK.add_discount(discount)

            elif user_input == 2:
                SDK.get_customers()
                customer_id = int(input('выберите покупателя:\n '))
                SDK.get_discount_by_customer_id(customer_id)

            elif user_input == 3:
                try:
                    SDK.get_customers()
                    customer_id = int(input('выберете покупателя:\n'))
                    date_start = str(input('введите дату начала интервала в формате дд/мм/гг \n'))
                    date_start = convert_str_to_date(date_start)
                    date_end = str(input('введите дату начала интервала в формате дд/мм/гг \n'))
                    date_end = convert_str_to_date(date_end)
                    SDK.get_discounts_by_interval(customer_id, date_start, date_end)

                except ValueError:
                    print('вы ввели не число, необходимо ввести число')


            elif user_input == 0:
                break

    elif user_input == 3:
        while True:
            SDK.get_products()
            print('''
1. изменить товар 
2. добавить товар 

0. выход
                    ''')
            user_input = int(input())
            if user_input == 1:  # change product
                SDK.get_products()
                product_name = input('введите название товара\n')
                product_obj = SDK.get_product_by_name(product_name)

                user_input = int(input('изменить товар? \n 1. да \n 2. нет \n'))

                if user_input == 1:  # change product realisation
                    product_new_name = input('введите новое название: \n')
                    product_new_price = input('введите новую цену: \n')
                    print(SDK.update_product(product_obj, product_new_name, product_new_price))
                    print('операция проведена успешно')

                elif user_input == 2:
                    break

            elif user_input == 2:  # add new product
                product_name = input('введите имя: \n')
                product_price = input('введите цену товара \n')
                product = Product(product_name, product_price)
                SDK.add_product(product)
                print('успешно добавлено')

            elif user_input == 0:
                break

    elif user_input == 4:
        while True:
            print('''
1. показать среднюю скидку для покупателей по определенному товару
2. показать средний процент скидок у покупателей
0. выход
            ''')
            user_input = int(input())
            if user_input == 1:  # show average discount for exact product
                SDK.get_products()
                product_id = int(input('выберите товар \n'))
                SDK.get_average_by_product(product_id, 'product_id')

            elif user_input == 2:
                customers = SDK.get_ids('customer_id', 'customers')
                for customer in customers:
                    SDK.get_discounts_average(customer, 'customer_id')

            elif user_input == 0:
                break
    elif user_input == 0:
        break
