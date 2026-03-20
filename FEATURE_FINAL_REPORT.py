# Import the total_sales function from another file to calculate total revenue
from FEATURE_TOTAL_SALES import total_sales

def generate_final_report(accumulated_orders):
    # This function prints a complete report of all orders made during the day.
    # It receives a tuple with all the registered orders.

    print()
    print(" FINAL REPORT ".center(50, "="))  # Print the report title
    print()

    # ── VALIDATION: CHECK IF THERE ARE ORDERS ─────────────────
    # If no orders were registered, show a message and stop the function
    if len(accumulated_orders) == 0:
        print("No orders registered yet.".center(50))
        print()
        return  # Exit the function early, nothing else to show

    # ══════════════════════════════════════════════════════════
    # SECTION 1: TOTAL ORDERS REGISTERED
    # Count how many orders are stored in the tuple
    # ══════════════════════════════════════════════════════════
    total_orders = len(accumulated_orders)  # len() counts the items in the tuple

    print(" 1. TOTAL ORDERS ".center(50, "-"))
    print()
    print("Total orders registered:".ljust(30), total_orders)  # Print the count
    print()

    # ══════════════════════════════════════════════════════════
    # SECTION 2: TOTAL REVENUE GENERATED
    # Call the total_sales function to add up all order subtotals
    # ══════════════════════════════════════════════════════════
    total = total_sales(accumulated_orders)  # This function returns the sum of all subtotals

    print()
    print(" 2. TOTAL REVENUE ".center(50, "-"))
    print()
    # f"${total:,}" formats the number with commas  example: $1,500,000
    print("Total revenue generated:".ljust(30), f"${total:,}")
    print()

    # ══════════════════════════════════════════════════════════
    # SECTION 3: ORDERS GROUPED BY CUSTOMER
    # Group all orders so we can see what each customer bought
    # ══════════════════════════════════════════════════════════
    print()
    print(" 3. ORDERS BY CUSTOMER ".center(50, "-"))
    print()

    # Create an empty dictionary to store orders grouped by customer name
    orders_by_customer = {}

    for order in accumulated_orders:
        customer_name = order["customer"]  # Get the customer name from the order

        # If this customer is not in the dictionary yet, create an empty tuple for them
        if customer_name not in orders_by_customer:
            orders_by_customer[customer_name] = ()

        # Add the current order to that customer's tuple
        # Tuples are immutable, so we build a new one each time
        orders_by_customer[customer_name] = orders_by_customer[customer_name] + (order,)

    # Now loop through each customer and print their orders
    for customer_name in orders_by_customer:
        customer_orders = orders_by_customer[customer_name]  # Get this customer's orders
        customer_total  = 0  # Start the customer total at zero

        print(f"  Customer: {customer_name}")
        print("  " + "-" * 40)

        # Loop through each order this customer made
        for order in customer_orders:
            customer_total = customer_total + order["Subtotal"]  # Add to customer total

            # Print the details of each order
            print("  Order ID:".ljust(22), order["id order"])
            print("  Product:".ljust(22),  order["product"])
            print("  Quantity:".ljust(22), order["quantity"])
            print("  Subtotal:".ljust(22), f"${order['Subtotal']:,}")
            print()

        # Print the total amount this customer spent
        print("=" * 40)
        print("  Customer total:".ljust(22), f"${customer_total:,}")
        print("=" * 40)
        print()

    # ══════════════════════════════════════════════════════════
    # SECTION 4: PRODUCTS SOLD TODAY
    # Group all orders by product to see how many units were sold
    # ══════════════════════════════════════════════════════════
    print()
    print(" 4. PRODUCTS SOLD TODAY ".center(50, "-"))
    print()

    # Create an empty dictionary to store data grouped by product name
    products_sold = {}

    for order in accumulated_orders:
        product_name = order["product"]  # Get the product name from the order

        # If this product is not in the dictionary yet, create counters for it
        if product_name not in products_sold:
            products_sold[product_name] = {
                "units_sold":   0,  # How many units were sold
                "total_earned": 0   # How much money was earned from this product
            }

        # Add the quantity and subtotal from this order to the product counters
        products_sold[product_name]["units_sold"]   = products_sold[product_name]["units_sold"]   + order["quantity"]
        products_sold[product_name]["total_earned"] = products_sold[product_name]["total_earned"] + order["Subtotal"]

    # Loop through each product and print its summary
    for product_name in products_sold:
        data = products_sold[product_name]  # Get the counters for this product

        print("  Product:".ljust(22),      product_name)
        print("  Units sold:".ljust(22),   data["units_sold"])
        print("  Total earned:".ljust(22), f"${data['total_earned']:,}")
        print()

    # Print the end of the report
    print("=" * 50)
    print(" END OF REPORT ".center(50, "="))
    print("=" * 50)
    print()