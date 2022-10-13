from functools import reduce


def findSum(arr):
    return reduce(lambda a, b: a+b, arr)



if __name__ == "__main__":
    size = int(input("Enter the size of the array : "))
    def verify(val):
        try:
            return int(val)
        except:
            print(f"Array can only contain numbers. Found '{val}'")
            exit()
    try:
        print("enter the values to add : ")
        arr = list(map(verify, input().split()))
    except:
        exit()

    print(findSum(arr[:size]))
