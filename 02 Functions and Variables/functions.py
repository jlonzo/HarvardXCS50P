#Declaring main body of the program
def main(): 
    name = input("Whats your name? ")
    hello(name)

#Function with Default parameter
def hello(to="World!"):
    print("Hello,", to)


#print(name)

#Function Call with no arguments
#hello()

#Function Call with arguments
#hello(name)

#calling main Prgram
main()