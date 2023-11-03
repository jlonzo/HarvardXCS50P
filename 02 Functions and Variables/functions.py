#name = input("Whats your name? ").strip().title()

#Split User's Name into First/Last Name
#first, last = name.split(" ")

# print(name)
# print("Hello,", name)
# print(f"Hello, {name}")

# Declaring main body of the program
def main():
    name = input("Whats your name? ")
    hello(name)

# Function with Default parameter
def hello(to="World!"):
    print("Hello,", to)

# calling main Program
main()