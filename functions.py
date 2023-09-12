#Declaring main body of the program
def main(): 
    #Function with Default parameter
    def hello(to="World!"):
        print("Hello, ", to)



name = input("Whats your name? ")
#print(name)

#Function Call with no arguments
hello()

#Function Call with arguments
hello(name)

#calling main Prgram
main()