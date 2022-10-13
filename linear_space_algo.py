from functools import reduce

def find_largest(arr):
    return reduce(lambda a,b:a if a>b else b,arr)



def find_lowest_positive_integer(arr):
    for v in range(1,find_largest(arr)+2):
        if v in arr:
            continue
        else:
            return v

if __name__ == "__main__":
    arr = [1,2,5,3,4]
    print(find_lowest_positive_integer(arr))


        


    