def register_client(accumulated_customers):
    # This function registers new customers into the system.
    # It receives a tuple with existing customers and returns it updated.

    keep_registering = "yes"  # Variable that controls if the loop keeps running

    # This loop keeps running as long as the user wants to add more customers
    while keep_registering == "yes":

        # Print a title header centered with "=" symbols
        print("CUSTOMER REGISTRATION".center(50, "="))

        # ── CUSTOMER ID VALIDATION ─────────────────────────────
        user_id = 0  # Start at 0 so the loop runs at least once

        # Keep asking until the user enters a valid positive number
        while user_id <= 0:
            try:
                # Ask the user to type a number and convert it to integer
                user_id = int(input("Enter an ID: "))

                # If the number is zero or negative, show an error
                if user_id <= 0:
                    print()
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")

            except ValueError:
                # This runs if the user types letters instead of numbers
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")

        # ── CUSTOMER NAME VALIDATION ───────────────────────────
        name = ""  # Start as empty so the loop runs at least once

        # Keep asking until the user types something
        while name == "":
            # .strip() removes accidental spaces before and after the text
            name = input("Customer name: ").strip()

            # If the user pressed Enter without typing, show an error
            if name == "":
                print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

        # ── CUSTOMER EMAIL VALIDATION ──────────────────────────
        email = ""  # Start as empty so the loop runs at least once

        # Keep asking until the user types something
        while email == "":
            # .strip() removes accidental spaces before and after the text
            email = input("Customer e-mail: ").strip()

            # If the user pressed Enter without typing, show an error
            if email == "":
                print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

        # ── SAVE THE NEW CUSTOMER ──────────────────────────────
        # Pack all collected data into a dictionary (like a data card per customer)
        customer = {
            "name":  name,
            "id":    user_id,
            "email": email
        }

        # Add the new customer to the tuple
        # Tuples cannot be modified, so we build a new one with both combined
        accumulated_customers = accumulated_customers + (customer,)

        # Show a success message to the user
        print()
        print("-" * 50)
        print("CUSTOMER SUCCESFULLY REGISTERED✅".center(50, "="))
        print("-" * 50)
        print()

        # Ask if the user wants to register another customer
        # .strip() removes spaces, .lower() converts to lowercase (Yes/YES = yes)
        keep_registering = input("Do you want to register another customer? yes/no: ").strip().lower()
        print()

    # Send back the updated tuple with all registered customers
    return accumulated_customers

