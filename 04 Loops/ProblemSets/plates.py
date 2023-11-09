import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # 2 chars MIN, 6 chars MAX
    if len(s) < 2 or len(s) > 6:
        return False

    # NO Punctiation marks or Spaces
    for c in s:
        if c in string.punctuation or c in [" "]:
            return False

    # starts with at least 2 letters
    # Numbers ONLY at the end of string and first number NOT zero
    i = 0
    f = 0 #1: DigitFound
    for c in s:
        if (i<=1) and not(c.isalpha()):
            #print("Rule: First two chars must be letters")
            return False
        elif c.isnumeric() and f == 0 and c != "0":
            #print("First digit (NON-ZERO) found")
            f = 1
        elif c.isnumeric() and f == 0 and c == "0":
            #print("Rule: First digit cant be ZERO")
            return False
        elif c.isalpha() and f == 1:
            #print("Rule: Letter after digit")
            return False
        i += 1

    # If all Rules passed RETURN TRUE
    return True

main()