# Python Program to find nth terms & Sum of Arithmetic of nth terms

# Sum of A.P. Series : Sn = n/2(2a + (n – 1) d)

# Tn term of A.P. Series: Tn = a + (n – 1) d

# where, a= first terms=2 ,3,100
#        d= constant difference =2,3
#        n= no of terms


# example: 2,4,6,8,10,... 
#          3,6,9,12,...
#          100,500,1000,...  thi is not an ap



a=int(input("PLZ ENTER THE first term "))
d=int(input("PLZ ENTER THE constant difference "))
n=int(input("PLZ ENTER THE no of terms "))

Tn= a + (n - 1)* d
print(Tn)


# 15 -5 =10
# 3,6,9,12