from customer import Customer
import SDK

customer = Customer("dagestan", "priorov", "moskov")

print(SDK.get_customer_by_name("NEWNAME"))
print(SDK.update_customer(customer, "Vasya"))
