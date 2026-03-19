def register_client(accumulated_tuple):
    keep_registering = "yes"
    
    while keep_registering == "yes":

        print("CUSTOMER REGISTRATION".center(50, "="))
        user_id = 0
        while  user_id <=0 :
            try:
                user_id = int(input("Enter an ID: "))

                if user_id <= 0:
                    print()
                    print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")

            except ValueError:
                print()
                print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")

        name = ""        
        while  name == "": 
                name = input("Customer name: ").strip()

                if name == "":
                    print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

        email = ""        
        while  email == "": 
                email = input("Customer e-mail: ").strip()

                if email == "":
                    print(f"{'❌ Error: Este campo no puede estar vacio. ❌':^65}")

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
