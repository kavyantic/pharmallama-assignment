from functools import reduce


def findSum(arr):
    return reduce(lambda a, b: a+b, arr)


if __name__ == "__main__":
    arrStr = input("please enter values to add : ")
    arr = arrStr.strip().split()
    for i, val in enumerate(arr):
        try:
            int(val)
            arr[i] = int(val)
            continue
        except:
            print(f"Array can only contain numbers found '{val}' at {i}")

            exit()

    print(findSum(arr))
