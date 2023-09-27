def main():
    due = 50
    accepts = []

    while due > 0:
        coin = int(input("Insert Coin: "))
        if (due-coin) | (coin) > 0:
            print("Due: " + str(50-coin))



main()