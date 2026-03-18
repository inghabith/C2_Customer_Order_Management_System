from script import register_products

products = ()

products = register_products(products)

for interant in products:
    print("PRODUCT INFORMATION".center(50, "-"))
    print()
    print("name".ljust(30), interant["name"])
    print("id".ljust(30), interant["id"])
    print("price".ljust(30), interant["price"])
    print()



