def check_orders(accumulated_orders):
    # This function displays all registered orders on screen.
    # It receives a tuple with all the orders saved in the system.

    # Print a title header centered with "=" symbols
    print(" ORDER LIST".center(50, "="))
    print()

    # ── VALIDATION: CHECK IF THERE ARE ORDERS ─────────────────
    # If the tuple is empty (no orders registered), show a message and stop
    if len(accumulated_orders) == 0:
        print("No orders registered")
        return  # Exit the function early, nothing else to show

    # ── DISPLAY EACH ORDER ─────────────────────────────────────
    # Loop through every order in the tuple one by one
    for iterant in accumulated_orders:

        # Print a separator line for each order
        print("ORDER INFORMATION".center(50, "-"))
        print()

        # Print each field of the order
        # .ljust(30) aligns the label text to the left using 30 spaces
        print("ID:".ljust(30),       iterant["id order"])   # Unique order number
        print("Name:".ljust(30),     iterant["customer"])   # Customer name
        print("Product:".ljust(30),  iterant["product"])    # Product name
        print("Quantity:".ljust(30), iterant["quantity"])   # Units ordered
        print("Subtotal:".ljust(30), iterant["Subtotal"])   # Total price for this order
        print()

    # Return the tuple unchanged — no modifications were made
    return accumulated_orders

