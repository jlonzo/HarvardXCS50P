def main():
    due = 50
    accepts = [25, 10, 5]

    while due > 0:
        print("Amount Due: " + str(due))
        coin = int(input("Insert Coin: "))
        if coin in accepts:
            due -= coin

    print("Change Owed: " + str(due * -1))               

main()