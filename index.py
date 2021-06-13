from customer import Customer
import SDK

customer = Customer("dagestan", "priorov", "moskov")

print(SDK.get_customers())
print(SDK.get_customer_by_name("KENTAVR"))