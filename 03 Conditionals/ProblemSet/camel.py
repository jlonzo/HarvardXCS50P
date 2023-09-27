def main():
    MyVar = str(input("camelCase: "))
    print("snake_case: " + toSnake(MyVar) )

def toSnake(v):
    i, f, snake = 0,0,""
    for c in v:         
        if c.isupper() and i > 0:
            snake += v[f:i] + "_"
            f = i
        i += 1

    snake += v[f:i]
    return snake

main()