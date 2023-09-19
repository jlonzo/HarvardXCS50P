def main():
    name = input("What's your name? ")
    #YourHouse(name)
    YourHouseV2(name)

def YourHouse(name):
    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")
    # elif name == "Hermione":
    #     print("Gryffindor")
    # elif name == "Ron":
    #     print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("Who?")

#Use of 'match'
def YourHouseV2(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        # case "Hermione":
        #     print("Gryffindor")
        # case "Ron":
        #     print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()