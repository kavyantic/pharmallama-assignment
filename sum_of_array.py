from functools import reduce

def findSum(arr):
    return reduce(lambda a,b:a+b,arr)

if __name__ =="__main__":
    print(findSum([2,4,3,4,2,4,7,4]))