def main():
    x = int(input("What's x? "))
    #if is_even(x):
    #if is_evenV2(x):
    if is_evenV3(x):
        print("Even")
    else:
        print("Odd")
        
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def is_evenV1(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Optimized (Pythonic) version
def is_evenV2(n):
    return True if n % 2 == 0 else False

#Optimized (Pythonic) version
def is_evenV3(n):
    #return (n % 2 == 0)
    return n % 2 == 0

main()