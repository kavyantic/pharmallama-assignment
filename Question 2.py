from functools import reduce

def find_largest(arr):
    return reduce(lambda a,b:a if a>b else b,arr)

def find_lowest_positive_integer(arr):
    for v in range(1,find_largest(arr)+2):
        if v in arr:
            continue
        else:
            return v
            
def main():
    arrStr = input("please enter array values : ")
    arr = arrStr.strip().split(" ")
    for i,val in enumerate(arr):
        try:
            int(val)
            arr[i] = int(val)
            continue
        except:
            print(f"Array can only contain numbers found '{val}' at {i}")
            return
    print(find_lowest_positive_integer(arr))

if __name__ == "__main__":
    main()
 

        


    