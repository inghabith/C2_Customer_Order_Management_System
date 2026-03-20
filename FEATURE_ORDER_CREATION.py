def create_order(accumulated_customers, accumulated_products, accumulated_orders):
    # This function creates new orders for the system.
    # It receives three tuples: existing customers, products, and orders.
    # It returns the updated tuple of orders.

    print()
    # Ask the user if they want to register an order before starting
    registro = input("¿Would you like to register an order? yes/no: ")

    # This loop keeps running as long as the user wants to add more orders
    while registro == "yes":

        # Print the section title
        print("=" * 60)
        print("ORDER REGISTRATION".center(60, "="))
        print("=" * 60)
        print()

        # ── SHOW ALL REGISTERED CUSTOMERS ─────────────────────
        # Display every customer stored in the tuple so the user can pick one
        print("REGISTERED CUSTOMERS".center(60))
        for cliente in accumulated_customers:
            print()
            print("ID:  ".ljust(30), cliente['id'])    # Customer ID number
            print("Name:".ljust(30), cliente['name'])  # Customer name
            print("-" * 50)
            print()

        # ── SHOW ALL AVAILABLE PRODUCTS ────────────────────────
        # Display every product stored in the tuple so the user can pick one
        print("PRODUCTS AVAILABLE".center(60))
        for producto in accumulated_products:
            print()
            print("ID:   ".ljust(30), producto['id'])     # Product ID number
            print("Name: ".ljust(30), producto['name'])   # Product name
            print("Price:".ljust(30), producto['price'])  # Product price
            print("-" * 50)

        print("-" * 50)

        # ── SELECT A CUSTOMER ──────────────────────────────────
        # Start as None so the loop runs at least once
        selected_customer = None

        # Keep asking until the user enters a valid customer ID
        while selected_customer is None:
            customer_option = int(input("Select the customer ID: "))

            # Search through the tuple to find the matching customer
            for customer in accumulated_customers:
                if customer["id"] == customer_option:
                    selected_customer = customer  # Customer found, save it

            # If no customer matched, ask again
            if selected_customer is None:
                print("❌ Customer ID not found, try again.")

        # ── SELECT A PRODUCT ───────────────────────────────────
        # Start as None so the loop runs at least once
        selected_product = None

        # Keep asking until the user enters a valid product ID
        while selected_product is None:
            product_option = int(input("Select the product ID: "))

            # Search through the tuple to find the matching product
            for product in accumulated_products:
                if product["id"] == product_option:
                    selected_product = product  # Product found, save it

            # If no product matched, ask again
            if selected_product is None:
                print("❌ Product ID not found, try again.")

        # ── GET QUANTITY ───────────────────────────────────────
        # Ask how many units of the product the customer wants
        quantity = int(input("Product quantity: "))

        # ── CALCULATE SUBTOTAL ─────────────────────────────────
        # Multiply the product price by the quantity to get the order total
        subtotal = selected_product["price"] * quantity

        # ── SAVE THE NEW ORDER ─────────────────────────────────
        # Pack all the order data into a dictionary (like a receipt)
        order_dictionary = {
            "id order": len(accumulated_orders) + 1,  # Auto-generate order ID based on how many orders exist
            "customer": selected_customer["name"],     # Name of the selected customer
            "product":  selected_product["name"],      # Name of the selected product
            "price":    selected_product["price"],     # Unit price of the product
            "quantity": quantity,                      # Number of units ordered
            "Subtotal": subtotal                       # Total price (price x quantity)
        }

        # Add the new order dictionary to the existing tuple of orders
        # Tuples are immutable, so we build a new one combining both
        accumulated_orders = accumulated_orders + (order_dictionary,)

        # Show a success message to the user
        print()
        print("-" * 50)
        print("ORDER SUCCESFULLY REGISTERED".center(50, "="))
        print("-" * 50)

        # Ask if the user wants to register another order
        registro = input("¿Would you like to register another order? yes/no: ")
        print()

    # Return the updated tuple with all registered orders
    return accumulated_orders