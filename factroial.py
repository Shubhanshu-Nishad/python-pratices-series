# Python program to find the factorial of a number provided by the user.

# The factorial function (symbol: !) says to multiply all whole numbers from our chosen number down to 1.

# Examples:

# 4! = 4 × 3 × 2 × 1 = 24
# 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040
# 1! = 1
# 0!=1



n=int(input("enter the num"))

fac=1

if n<0:
    print('the fac og negative no does not exit')
elif n==0:
    print('the fac of 0 is 1')
else:
    for i in range(1,n+1):
        fac=fac*i
    print("the fac is ",fac)

# 1*1=1
# 1*2=2
# 2*3=6
# 6*4=24



s=n-1
t=s*d
Tn= a+t
print(Tn)



# Tn= (a + (n - 1 )* d )
# print(Tn)

# print(sn)

total = 0
value = a
print("Arithmetic Progression Series : ", end = " ")
for i in range(n):
    print("%d + " %value, end = " ")
    total = total + value
    value = value + d

print("\nThe Sum of Arithmetic Progression Series upto %d = %d " %(n, total))