# print("Hello, World!)

# Ask the user for their name
# name = input("Whats your name? ")
# print("Hello, name!)

# Inline String Method Calling
name = input("Whats your name? ").strip().title()

# Trim the String
# name = name.strip()
# Capitalize the String
# name = name.capitalize()
# Camelcase the String
# name = name.title()
# Split string
first, last = name.split(" ")
print(f"Hello, {first}")

# Trim and Camelcase the String variable
# name = name.strip().title()

# Pseudocode: Write the steps first then fill the gaps with actual code
# Print hello
# print("hello,")
# Print the name inputted
# print(name)

# Two ways to concatenate strings in the print function
# print("Hello, "+name+"!")
# print("Hello,",name) #Comma separated variables will add a blank space between strings
print(f"Hello, {name}")

# Another way to print strings by overriding the default value for end of line
# print("Hello ", end="")
# print(name)

# Another way to print strings by changing the default value for separator
# print("Hello,",name, sep="??")

# Use of DoubleQuotes in Strings
# print('Hello "friend"')
# print("Hello \"friend\"")
