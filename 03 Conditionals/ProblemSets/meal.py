def main():
    time = input("What time is it? ")
    ftime = convert(time)
    if 7.0 <= ftime <= 8.0:
        print("breakfast time")
    elif 12.00 <= ftime <= 13.00:
        print("lunch time")
    elif 18.00 <= ftime <= 19.00:
        print("dinner time")
    
def convert(t):
    h,m = t.split(":")
    ft = float(h) + round((float(m)/60),2)
    return ft

if __name__ == "__main__":
    main()