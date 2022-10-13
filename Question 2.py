from functools import reduce


def find_largest(arr):
    return reduce(lambda a,b:a if a>b else b,arr)

def find_lowest_positive_integer(arr):
    # finding largest in the array to loop through and
    #  adding 2 because array might contain all possible positive integer 
    for v in range(1,find_largest(arr)+2):
        # checking if v exists in the array, if not then we got our lowest positive integer 
        if v in arr:
            continue
        else:
            return v
            
def main():
    def verify(val):
        try:
            return int(val)
        except:
            print(f"Array can only contain numbers. Found '{val}'")
            exit()
    try:
        arr = list(map(verify, input().split()))
    except:
        exit()

    print(find_lowest_positive_integer(arr))

if __name__ == "__main__":
    main()
 

        


    