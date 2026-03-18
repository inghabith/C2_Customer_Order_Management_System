def register_client(accumulated_tuple):
    keep_registering = "yes"
    
    while keep_registering == "yes":

        print("CUSTOMER REGISTRATION".center(50, "="))

        user_id = int(input("Enter an ID: "))
        name = input("Enter customer name: ")
        email = input("Enter customer e-mail: ")


        customer = {
            "name" : name,
            "id"     : user_id,
            "email"  : email
        }

        accumulated_tuple = accumulated_tuple + (customer,)
        print()
        print("-" * 50)
        print("CUSTOMER SUCCESFULLY REGISTERED✅".center(50, "="))
        print("-" * 50)
        print()
        keep_registering = input("Do you want to register another customer? yes/no: ").strip().lower()
        print()

    return accumulated_tuple
    
