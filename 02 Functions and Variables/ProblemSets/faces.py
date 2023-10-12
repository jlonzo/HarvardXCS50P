def main():
    MyString = str(input("Input your String: "))
    print(convert(MyString))


def convert(toConvert):
    toConvert = toConvert.replace(":)", "🙂")
    toConvert = toConvert.replace(":(", "🙁")
    return toConvert


main()
