#Print "meow" three times
print("meow")
print("meow")
print("meow")

#while
i = 3
while i != 0:
    print("meow")
    i -= 1

# for using a list
for i in [0, 1, 2]:
    print("meow")

# for using range
#for i in range(3):
# for correctness use _ instead of a var name when not used
# about a variable
for _ in range(3): 
    print("meow")

#pythonic way to print a message N number of times
print("meow\n" * 3, end="")

# Python Inifinite loop to ask user for a positive number
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

#another way
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#another way using functions
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's the value of n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()