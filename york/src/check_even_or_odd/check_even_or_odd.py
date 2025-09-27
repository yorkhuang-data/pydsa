
def isEven(n):
    # taking bitwise and of n with 1
    if (n & 1) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    while(True):
        n = int(input("Input an integer: "))
        if isEven(n):
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")