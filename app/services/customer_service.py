customers = [
    {
        "id": 1,
        "name": "John",
        "email": "john@example.com",
        "phone": "9876543210"
    },
    {
        "id": 2,
        "name": "Mary",
        "email": "mary@example.com",
        "phone": "9876501234"
    }
]

nextCustomerId = 3

# GET all customers
def getAllCustomers():
    return customers

# GET one customer
def getCustomerById(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    return None

# CREATE a customer
def createCustomer(name, email, phone):
    global nextCustomerId

    newCustomer = {
        "id": nextCustomerId,
        "name": name,
        "email": email,
        "phone": phone
    }

    customers.append(newCustomer)
    nextCustomerId += 1

    return newCustomer

# UPDATE a customer
def updateCustomer(customer_id, name, email, phone):
    for customer in customers:
        if customer["id"] == customer_id:
            customer["name"] = name
            customer["email"] = email
            customer["phone"] = phone

            return customer

    return None

# DELETE a customer
def deleteCustomer(customer_id):
    for index, customer in enumerate(customers):
        if customer["id"] == customer_id:
            deleteCustomer = customers.pop(index)
            return deleteCustomer

    return None
