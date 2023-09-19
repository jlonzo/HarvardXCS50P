def main ():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    #useof_if(x,y)
    #useof_or(x,y)
    useof_notequal(x,y)

def useof_if(x,y):
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    #elif x == y:
    else:
        print("x is equal than y")

#Use of 'or'
def useof_or(x,y):
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal than y")

#USe of not equal
def useof_notequal(x,y):
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal than y")

main()