def register_products(products):

    keep_registering = "yes"

    products= (
        {"id": 1, "name": "Manzana", "price": 2000},
        {"id": 2, "name": "Pera", "price": 3000}
    )

    while keep_registering == "yes":

#validacion de datos para cada input "product_name, product_price"
        product_id = 0
        while  product_id <=0 :
            try:
                product_id = int(input("Enter product ID: "))

                if product_id <= 0:
                    print()
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")

            except ValueError:
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")
               
# validation on products name.
        product_name = ""
        while  product_name == "": 
                
                product_name = input("Enter product name: ").strip()

                if product_name == "":
                    print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

# ===== Validation on  product_price 
        product_price = 0
        while  product_price <=0:
            try:
                product_price = int(input("Enter unit price: $"))

                if product_price <= 0:
                    print("="*60)
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")
                    print("="*60)

            except ValueError:
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")

        dictionary = {
                "id": product_id,
                "name": product_name,
                "price": product_price
            }

        products = products + (dictionary,)

        keep_registering = input("Would you like to enter another product? yes/no: " ).strip().lower()

    return products



