def main():
    vowels = ["A","E","I","O","U"]
    tweet = input("Input: ")

    for c in tweet:
        u = c.upper()
        if u in vowels:
            tweet = tweet.replace(c, "")
    
    print("Output: " + tweet)

main()