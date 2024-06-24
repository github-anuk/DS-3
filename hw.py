
def power(n,x):
    if n == 0 :
        return 0 
    else :
        return n**x

n = int(input("NUMBER "))
x = int(input("POWER "))
print(power(n,x))