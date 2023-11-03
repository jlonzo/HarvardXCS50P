def main():
    answer = input("What is the answer to the Great Question of Life,"
                    " the Universe, and Everything? ")
    eval_answer(answer)

def eval_answer(a):
    if (a.upper() == "FORTY-TWO") \
        or (a.upper() == "FORTY TWO") or \
        (int(a) == 42):
        print("Yes")
    else:
        print("No")

main()