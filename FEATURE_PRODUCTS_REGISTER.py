def register_products(accumulated_products):
    # This function adds new products to the system.
    # It receives a tuple with the existing products and returns it updated.

    keep_registering = "yes"

    # Pre-loaded products so the system starts with data already available
    accumulated_products = (
        {"id": 101, "name": "Manzana", "price": 2000},
        {"id": 201, "name": "Pera", "price": 3000}
    )

    # This loop keeps running as long as the user wants to add more products
    while keep_registering == "yes":

        print("PRODUCT REGISTRATION".center(50, "="))

        # ── PRODUCT ID VALIDATION ──────────────────────────────
        # Start at 0 so the loop runs at least once
        product_id = 0

        # Keep asking until the user enters a valid positive number
        while product_id <= 0:
            try:
                product_id = int(input("Enter product ID: "))

                # Check that the number is greater than zero
                if product_id <= 0:
                    print()
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")

            except ValueError:
                # This runs if the user types letters instead of numbers
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")

        # ── PRODUCT NAME VALIDATION ────────────────────────────
        # Start as empty string so the loop runs at least once
        product_name = ""

        # Keep asking until the user types something (not just spaces)
        while product_name == "":
            product_name = input("Enter product name: ").strip()  # .strip() removes accidental spaces

            # If the user pressed Enter without typing, show an error
            if product_name == "":
                print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

        # ── PRODUCT PRICE VALIDATION ───────────────────────────
        # Start at 0 so the loop runs at least once
        product_price = 0

        # Keep asking until the user enters a valid positive price
        while product_price <= 0:
            try:
                product_price = int(input("Enter unit price: $"))

                # Check that the price is greater than zero
                if product_price <= 0:
                    print("=" * 60)
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")
                    print("=" * 60)

            except ValueError:
                # This runs if the user types letters instead of numbers
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")

        # ── SAVE THE NEW PRODUCT ───────────────────────────────
        # Store the collected data in a dictionary (like a small data card)
        dictionary = {
            "id": product_id,
            "name": product_name,
            "price": product_price
        }

        # Show a success message to the user
        print()
        print("-" * 50)
        print("PRODUCT SUCCESFULLY REGISTERED✅".center(50, "="))
        print("-" * 50)
        print()

        # Add the new product dictionary to the existing tuple of products
        # Tuples are immutable, so we create a new one combining both
        accumulated_products = accumulated_products + (dictionary,)

        # Ask the user if they want to register another product
        keep_registering = input("Would you like to enter another product? yes/no: ").strip().lower()

    # Return the updated tuple with all registered products
    return accumulated_products

