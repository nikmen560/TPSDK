from customer import Customer
import SDK

customer = Customer("dagestan", "priorov", "moskov")
print(SDK.add_customer(customer))