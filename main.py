# ── IMPORTS ───────────────────────────────────────────────────
# Each line brings in a function from another file so we can use it here.
# Without these imports, the main menu would not know what to do when the user picks an option.
from FEATURE_CUSTOMER_REGISTER import register_client      # Function to register new customers
from FEATURE_FINAL_REPORT import generate_final_report     # Function to print the final report
from FEATURE_PRODUCTS_REGISTER import register_products    # Function to register new products
from FEATURE_ORDER_CREATION import create_order            # Function to create new orders
from FEATURE_CHECK_ORDERS import check_orders              # Function to display all orders
from FEATURE_TOTAL_SALES import total_sales                # Function to calculate total revenue

# ── STARTING DATA ──────────────────────────────────────────────
# These three variables start as empty tuples.
# They will grow as the user registers customers, products, and orders.
# We use tuples because the project does not allow lists.
accumulated_products  = ()  # Stores all registered products
accumulated_orders    = ()  # Stores all registered orders
accumulated_customers = ()  # Stores all registered customers

# ── WELCOME MESSAGE ────────────────────────────────────────────
# This prints a decorated welcome banner when the program starts.
# It only shows once, before the menu loop begins.
print(f"""
    ╔═══════════════════════════════════════════════════════════╗
                    🛒 Pricesmart Riwi 🛒
    🌷 Welcome to the Customer Order Management System! 🌷
    ╚═══════════════════════════════════════════════════════════╝""")

# ── MAIN MENU LOOP ─────────────────────────────────────────────
# Menu starts as "yes" so the loop runs at least once.
# The loop keeps running until the user types "no" at the end.
Menu = "yes"

while Menu == "yes":

    try:
        # Show the main menu and ask the user to pick an option.
        # int() converts the user's input from text to a number.
        Option = int(input(f"""{"-"*24} MAIN MENU {"-"*25} 
1) 🤵  Enter Costumer 
2) 🥦  Enter Product 
3) 🧾  Create Order
4) 🔍  View Orders
5) 📋  Generate Final Report
{"="*60}
~ Please select an option:
➤  """))

        # ── RANGE VALIDATION ───────────────────────────────────
        # Check if the number is outside the valid range (1 to 5).
        # If it is, show an error and skip back to the top of the loop.
        if Option < 1 or Option > 6:
            print(f"\n{'❌ ERROR: Please enter a valid number ❌':^60}\n")
            continue  # Go back to the top of the while loop

    except ValueError:
        # ── TYPE VALIDATION ────────────────────────────────────
        # This runs if the user types letters instead of a number.
        # int() cannot convert letters, so Python raises a ValueError.
        # We catch it here and show a friendly error message.
        print(f"\n{'❌ ERROR: Please enter a valid integer ❌':^60}\n")
        continue  # Go back to the top of the while loop

    # ── OPTION 1: REGISTER A CUSTOMER ─────────────────────────
    # Call the register_client function and save the updated tuple.
    # The new customer gets added inside that function and returned here.
    if Option == 1:
        accumulated_customers = register_client(accumulated_customers)

    # ── OPTION 2: REGISTER A PRODUCT ──────────────────────────
    # Call the register_products function and save the updated tuple.
    # The new product gets added inside that function and returned here.
    elif Option == 2:
        accumulated_products = register_products(accumulated_products)

    # ── OPTION 3: CREATE AN ORDER ──────────────────────────────
    # Call the create_order function and pass all three tuples.
    # It needs customers and products to build the order,
    # and it returns the updated orders tuple with the new order added.
    elif Option == 3:
        accumulated_orders = create_order(accumulated_customers, accumulated_products, accumulated_orders)

    # ── OPTION 4: VIEW ALL ORDERS ──────────────────────────────
    # Call check_orders to display every registered order on screen.
    # Then call total_sales to calculate and store the total revenue.
    elif Option == 4:
        check_orders(accumulated_orders)
        total = total_sales(accumulated_orders)  # Save the total in case it is needed later

    # ── OPTION 5: GENERATE FINAL REPORT ───────────────────────
    # Call generate_final_report to print the complete summary of the day.
    # This includes total orders, total revenue, orders by customer, and products sold.
    elif Option == 5:
        generate_final_report(accumulated_orders)

    # ── ASK TO RETURN TO MENU ──────────────────────────────────
    # After every option, ask the user if they want to go back to the menu.
    # .strip() removes accidental spaces, .lower() converts YES/Yes to yes.
    # If the user types "no", the while condition becomes False and the loop ends.
    Menu = input("\nDo you want to return to the main menu? yes/no : ").strip().lower()

# ── GOODBYE MESSAGE ────────────────────────────────────────────
# This line only runs when the loop is finished (user typed "no").
# It prints a farewell message and the program ends.
print("\n✅ Thank you for using Pricesmart Riwi! Goodbye! 👋\n")


