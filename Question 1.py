from functools import reduce

# using reduce function to find the some
def findSum(arr):
    return reduce(lambda a, b: a+b, arr)



if __name__ == "__main__":
    size = int(input())

    # function to verify whether the strings in the array are digits or not 
    def verify(val):
        try:
            return int(val)
        except:
            print(f"Array can only contain numbers. Found '{val}'")
            exit()
    try:
        # input().split() will take input and split the string by its white spaces 
        # Using map function to apply validation over every splitted string 
        arr = list(map(verify, input().split()))
    except:
        exit()

    print(findSum(arr[:size]))
