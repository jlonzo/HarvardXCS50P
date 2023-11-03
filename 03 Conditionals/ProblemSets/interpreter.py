def main():
    ex = input("Expression: ").strip()
    x,op,y = ex.split(" ")
    # print(x)
    # print(op)
    # print(y)
    print(eval_op(float(x),float(y),op))

def eval_op(a,b,o):
    match o:
        case "+":
            return(a+b)
        case "-":
            return(a-b)
        case "*":
            return(a*b)
        case "/":
            return (a/b)

main()