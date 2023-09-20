# x = input("What's x? ")
# y = input("What's y? ")
# z = int(x) + int(y)
# print(z)

#Nested Function Calls
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Rounding numbers
#z = round(x+y)

#Formatting numbers (Commas-sepparated number)
#print(f"{z:,}")

#Divisions with Rounding
#z = round(x/y,2)

#Another way of round numbers
#z = x/y
#print(f"{z:.2f}")


#print(z)

# -- Calculator with Functions
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()    