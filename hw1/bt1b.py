n= str(input("user name "))
m= str(input("password "))
if n == "techkids":
    if m == "codethechange":
        print("Welcome,superuser")
    else:
        print("Invalid password")
else: 
    print("You are not superuser")