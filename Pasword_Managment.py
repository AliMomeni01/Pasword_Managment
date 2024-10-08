from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("D:\\Python Übung\\Folge8\\mykey.key","wb")as f:
#         f.write(key)
# write_key() 

def load_key():
    with open("D:\\Python Übung\\Folge8\\mykey.key","rb") as f:
        return f.read()
    
key = load_key()    
fernet = Fernet(key)

def add_password(username,password):
    with open("D:\\Python Übung\\Folge8\\password3.txt","a") as f : 
        encrypted_pass = fernet.encrypt(password.encode()).decode()
        f.write(f"{username}|{encrypted_pass}\n")     
    print("Added")
def view_pass():
        with open("D:\\Python Übung\\Folge8\\password3.txt","r") as f : 
            for item in f:
                item = item.rstrip()
                username, ecncrypted_password = item.split("|")   
                password = fernet.decrypt(ecncrypted_password).decode()     
                print(f"Username: {username}|Password: {password}")
while True:

    user_input = input("Enter the option(v:view, a:add, q:quit)")
    if user_input == "v":
        print("Your passwords are as follow")
        view_pass()

    elif user_input == "a":
        print("Let's add a new username-password ")

        username = input("Enter new username:")
        password = input("Enter new password")
        add_password(username,password)
        
    elif user_input == "q":
        print("close")   
        break
    else:
        print("Wrong model")
        