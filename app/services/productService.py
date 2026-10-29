# Temporary in-memory data
products = [
    {
        "id": 1,
        "name": "Keyboard",
        "price": 1200
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 500
    }
]

nextProductId = 3

def getAllProducts():
    return products

def getProductById(product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None

def createProduct(name, price):
    global nextProductId

    newProduct = {
        "id": nextProductId,
        "name": name,
        "price": price
    }

    products.append(newProduct)
    nextProductId += 1

    return newProduct

def updateProduct(product_id, name, price):
    for product in products:
        if product["id"] == product_id:
            product["name"] = name
            product["price"] = price

            return product
        
    return None

def deleteProduct(product_id):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)

            return deleted_product
        
    return None
        