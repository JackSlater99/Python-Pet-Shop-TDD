# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,transaction_amount):
    pet_shop["admin"]["total_cash"] += (transaction_amount)
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
     pet_shop["admin"]["pets_sold"] += (pets_sold)
     
def get_stock_count(pet_shop):
     return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_by_breed = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            pet_by_breed.append(pet)
    return pet_by_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pets in pet_shop["pets"]:
        if pets["name"] == name:
            pet_shop["pets"].remove(pets)
    return pet_shop

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return pet_shop

def get_customer_cash(customers):
    customer_cash = customers["cash"]
    return customer_cash

def remove_customer_cash(customers, transaction_amount):
    customers["cash"] -= (transaction_amount)
    
def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def find_pet_price(pet_store, pet):
    pet_dict = pet
    if isinstance(pet, str):
        pet_dict = find_pet_by_name(pet_store, pet)
    price = pet_dict['price']
    return price

def customer_can_afford_pet(customer, pet_store, pet):
    print(pet)
    return get_customer_cash(customer) >= find_pet_price(pet_store, pet)
    

def sell_pet_to_customer(pet_store, pet, customer):
    customer_can_afford_pet(customer, pet_store, pet)
    price = pet["price"]
    add_pet_to_customer(customer, pet)
    increase_pets_sold(pet_store, 1)
    remove_customer_cash(customer, price)
    add_or_remove_cash(pet_store, price)
