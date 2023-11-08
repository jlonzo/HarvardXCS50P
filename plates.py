def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    r = True
    # starts with at least 2 letters
    
    #maximum of 6 characters
    n = (len(s))
    print("Value of n is: ",n)
    if 2 >= n <= 6:
        r = False
        print("Result is: ",r)
    
    return r

main()


# score = int(input("Input: "))
    
# if score < 2:
#     print("False")
# if score > 6:
#     print("False")