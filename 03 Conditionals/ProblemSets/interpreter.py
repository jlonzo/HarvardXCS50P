def main():
    ex = input("Expression: ").strip()
    x,y,z = ex.split(" ")
    print(round(eval_op(float(x),float(z),y),2))

def eval_op(a,b,o):
    match o:
        case "+":
            return(a+b)
        case "-":
            return(a-b)
        case "*":
            return(a*b)
        case "/":
            if b  != 0:
                return (a/b)

main()