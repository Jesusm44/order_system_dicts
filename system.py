"""
Simple Order Management System (CLI)

Features:
- User management
- Product management
- Order creation
- Order deletion
- ID uniqueness enforced via sets

Constraints:
- No functions or classes (procedural design)
- In-memory storage only
"""

users = []
products = []
orders = []

user_ids = set()
product_ids = set()
order_ids = set()


while True:

    print("\n=== MENU ===")
    print("1. Add user")
    print("2. Add product")
    print("3. Create order")
    print("4. Show orders")
    print("5. Delete order")
    print("6. Exit")

    option = input("Select an option: ")

    # -----------------------------
    # USER CREATION
    # -----------------------------
    if option == "1":
        user_id = int(input("User ID: "))

        if user_id in user_ids:
            print("Error: ID already exists")
            continue

        name = input("Name: ").strip()

        if not name:
            print("Error: Invalid name")
            continue

        user = {
            "id": user_id,
            "name": name
        }

        users.append(user)
        user_ids.add(user_id)

        print("User created successfully")

    # -----------------------------
    # PRODUCT CREATION
    # -----------------------------
    elif option == "2":
        product_id = int(input("Product ID: "))

        if product_id in product_ids:
            print("Error: ID already exists")
            continue

        name = input("Product name: ").strip()
        price = int(input("Price: "))
        stock = int(input("Stock: "))

        if not name:
            print("Error: Invalid product name")
            continue

        if price < 0 or stock < 0:
            print("Error: Price and stock must be non-negative")
            continue

        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "stock": stock
        }

        products.append(product)
        product_ids.add(product_id)

        print("Product created successfully")

    # -----------------------------
    # ORDER CREATION
    # -----------------------------
    elif option == "3":
        order_id = int(input("Order ID: "))
        user_id = int(input("User ID: "))
        product_id = int(input("Product ID: "))

        if order_id in order_ids:
            print("Error: Order ID already exists")
            continue

        if user_id not in user_ids:
            print("Error: User not found")
            continue

        if product_id not in product_ids:
            print("Error: Product not found")
            continue

        quantity = int(input("Quantity: "))

        found = False
        sufficient_stock = True
        order_items = []
        total = 0

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
            print("Error: Product not found")
            continue

        if not sufficient_stock:
            print("Error: Insufficient stock")
            continue

        order = {
            "id": order_id,
            "user_id": user_id,
            "items": order_items,
            "total": total
        }

        orders.append(order)
        order_ids.add(order_id)

        print("Order created successfully")

    # -----------------------------
    # DISPLAY ORDERS
    # -----------------------------
    elif option == "4":
        if not orders:
            print("No orders available")
            continue

        for order in orders:
            print(f"\nOrder ID: {order['id']}")
            print(f"User ID: {order['user_id']}")
            print(f"Items: {order['items']}")
            print(f"Total: {order['total']}")

    # -----------------------------
    # DELETE ORDER
    # -----------------------------
    elif option == "5":
        target_id = int(input("Order ID to delete: "))

        if target_id not in order_ids:
            print("Error: Order not found")
            continue

        for order in orders:
            if order["id"] == target_id:
                orders.remove(order)
                order_ids.remove(target_id)
                print("Order deleted successfully")
                break

    # -----------------------------
    # EXIT
    # -----------------------------
    elif option == "6":
        print("Exiting...")
        break

    else:
        print("Invalid option")







