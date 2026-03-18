def register_products(products):

    keep_registering = "yes"

    products= (
        {"id": 1, "name": "Manzana", "price": 2000},
        {"id": 2, "name": "Pera", "price": 3000}
    )

    while keep_registering == "yes":

        product_id = int(input("Enter product ID: "))

        
        product_name = input("Enter product name: ")
        product_price = int(input("Enter unit price: $"))

        dictionary = {
                "id": product_id,
                "name": product_name,
                "price": product_price
            }

        products = products + (dictionary,)

        keep_registering = input(
            "Would you like to enter another product? yes/no: "
        ).strip().lower()

    return products





