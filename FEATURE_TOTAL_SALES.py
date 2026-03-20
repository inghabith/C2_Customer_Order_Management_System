def total_sales(accumulated_orders):
    # This function calculates the total money earned from all orders.
    # It receives a tuple with all registered orders and returns the final sum.

    total = 0  # Start the counter at zero before adding anything

    # Loop through every order in the tuple one by one
    for iterant in accumulated_orders:

        # Add the subtotal of each order to the running total
        # += means: total = total + iterant["Subtotal"]
        total += iterant["Subtotal"]

    # Return the final sum so other functions can use it
    return total
    
    
     

