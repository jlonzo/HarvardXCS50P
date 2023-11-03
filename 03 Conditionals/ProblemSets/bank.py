def main():
    greeting = input("Greetin: ")
    loan_amount(greeting)

def loan_amount(val):
    if(val[0:5].upper() == "HELLO"):
        print("$0")
    elif (val[0:1].upper() == "H"):
        print("$20")
    else:
        print("$100")

main()    
