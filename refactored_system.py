from typing import Any, Literal, LiteralString

users:list[Any] = []
users_ids:set[int] = set()

products:list[Any] = []
products_ids:set[int] = set()

orders:list[Any] = []
orders_ids:set[int] = set()

def add_user(id:int, name:str)-> None | dict[str | int, Any]:
    if not isinstance(id, int):
        return None

    if not isinstance(name, str):
        return None

    if id not in range(0,100):
        return None

    if id in users_ids:
        return None

    if name.strip() == "":
        return None
    
    new_user:dict[str|int, Any] = {
        "id": id,
        "name": name
    }

    users.append(new_user)
    users_ids.add(id)
    return new_user

def create_product(id:int, name:str, price:int|float, stock:int)-> None | dict[str, Any]:
    if not isinstance(id, int):
        return None

    if not isinstance(name, str):
        return None

    if not isinstance(price, (int, float)):
        return None

    if not isinstance(stock, int):
        return None

    if id in products_ids:
        return None

    if id not in range(0,101):
        return None

    if name.strip() == "":
        return None

    if price < 0 or stock < 0:
        return None

    product:dict[str,Any] ={
        "id":id,
        "name":name,
        "price":price,
        "stock":stock
    }

    products.append(product)
    products_ids.add(id)
    return product

def create_order(order_id, user_id, product_id,quantity) -> None | dict[str | int, Any]:
    found = False
    sufficient_stock = True
    order_items:list[Any] = []
    total = 0

    if not isinstance(order_id,int):
        return None

    if not isinstance(quantity, int):
        return None

    def validate_order()-> bool:
        if order_id in orders_ids:
            return False
        if user_id not in users_ids:
            return False
        if product_id not in products_ids:
            return False
        return True

    if not validate_order():
        return None

    for product in products:
        if product["id"] == product_id:
            found = True

            if product["stock"] >= quantity:
                total += product["price"] * quantity
                product["stock"] -= quantity

                order_items.append({
                    "id": product["id"],
                    "quantity": quantity,
                    "unit_price": product["price"]
                })
            else:
                sufficient_stock = False
            break

    if not found:
        return None

    if not sufficient_stock:
        return None

    order:dict[str|int,Any] = {
        "id":order_id,
        "user_id": user_id,
        "items": order_items,
        "total":total
    }

    orders.append(order)
    orders_ids.add(order_id)
    return order

def print_order(orders) -> None | str:
    if not orders:
        print("No orders available")
        return None

    for order in orders:
        id:int = order["id"]
        user:int = order["user_id"]
        items:list[dict[str,Any]] = order["items"]
        total:int = order["total"]

        print (f"""
------------------
Order ID: {id}
User ID:  {user}
Items:    {items}
Total:    {total}
------------------ """)

def delete_order(orders,target_id) -> bool:
    if target_id not in orders_ids:
        return False

    for order in orders:
        if order["id"] == target_id:
            orders.remove(order)
            orders_ids.remove(target_id)
            return True

    return False

while True:
    print("Choose an option")
    option = int(input(f"""
1. Add user
2. Create products
3. Create order
4. Print order
5. Delete order
6. Exit"""))

    if option == 1:
        id = int(input("Enter the ID you are going to add: "))
        name = str(input("Enter the username you are going to add: "))

        user: None | dict[str | int, Any] = add_user(id,name)

        if user:
            print(f'The user, {user["name"]}, has been successfully created')
    elif option == 2:
        id = int(input("Enter the ID of the product you want to create: "))
        name = str(input("Enter the name of the product you want to create: "))
        price = int(input("Enter the price of the product you want to create: "))
        stock = int(input( "Enter the stock of the product you want to create: "))

        new_product = create_product(
            id = id,
            name =name,
            price=price,
            stock=stock
        )

        if new_product is not None:
            print(f'The product, {new_product["name"]}, has been successfully added')
    elif option == 3:
        order_id = int(input("Create the order ID: "))
        user_id = int(input("Enter the ID of the user requesting the product: "))
        product_id = int(input("usuarioEnter the ID of the product requested by the user: "))
        quantity = int(input("Enter the amount the user wants: "))

        new_order = create_order(
            order_id=order_id,
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )

        if new_order is not None:
            print(f'Order NO. {new_order["id"]}, has been created')
    elif option == 4:
        print_order(orders=orders)
    elif option == 5:
        target_id = int(input("Enter the order number for the product you want to delete: "))

        delete: bool = delete_order(orders,target_id)
        if delete:
            print(f'The command NO. {target_id}, has been deleted')
        else:
            print("ERROR: Order not found")
            break
    elif option == 6:
        print("Leaving the program")
        break
    else:
        print("ERROR: Invalid option")
        break