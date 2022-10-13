def prime(val):
    for i in range(2,val):
        if val%i==0:return False
    return True
print([i*i for i in range(2,101) if(prime(i))])


