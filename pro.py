FILE_NAME = "users.txt"

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip():
                    u, p = line.strip().split(",")
                    if u == username:
                        print("Username already exists!\n")
                        return
    except FileNotFoundError:
        pass  # file will be created later

    with open(FILE_NAME, "a") as f:
        f.write(username + "," + password + "\n")

    print("Registration successful!\n")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip():
                    u, p = line.strip().split(",")
                    if u == username and p == password:
                        print("Login successful!\n")
                        return
    except FileNotFoundError:
        print("No users registered yet!\n")
        return

    print("Invalid credentials!\n")


while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice\n")