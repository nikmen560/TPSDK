from customer import Customer
import SDK

# customer = Customer("dagestan", "priorov", "moskov")

# print(SDK.get_customer_by_name("NEWNAME"))
# print(SDK.update_customer(customer, "Vasya"))

while True:
    print('''
    1. информация о покупателях
    2. 
    3.
    4.
    ''')

    user_input = int(input())

    if user_input == 1:
        while True:
            print(SDK.get_customers())

            print('''
            1. изменить покупателя
            2. добавить покупателя
            
            0. выход
            ''')

            user_input = int(input())

            if user_input == 1:
                while True:
                    print(SDK.get_customers())
                    customer_name = input('введите имя покупателя \n')
                    customer_obj = SDK.get_customer_by_name(customer_name)

                    user_input = int(input('изменить покупателя? \n 1. да \n 2. нет \n'))

                    if user_input == 1:
                        customer_new_name = input('введите новое имя: \n')
                        customer_new_surname = input('введите новую фамилию: \n')
                        customer_new_address = input('введите новый адрес: \n')
                        print(SDK.update_customer(customer_obj, customer_new_name, customer_new_surname, customer_new_address))

                    if user_input == 2:
                        break
            else:
                break
