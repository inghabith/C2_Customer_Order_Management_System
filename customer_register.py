
def register_client(accumulated_tuple):
    keep_registering = "yes"
    
    while keep_registering == "yes":

        print("customer registration".center(50, "="))
        print("-" * 50)

        user_id = input("Enter your ID: ")
        name = input("type your name: ")
        email = input("enter your email: ")


        customer = {
            "nombre" : name,
            "id"     : user_id,
            "email"  : email
        }

        accumulated_tuple = accumulated_tuple + (customer,)
        print("-" * 50)
        print("customer successfully registered✅".center(50, "="))
        print("-" * 50)
        keep_registering = input("Do you want to register another customer? yes/no: ").strip().lower()

    return accumulated_tuple
    
clients = register_client(())
