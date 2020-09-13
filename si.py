# Simple interest is a quick and easy method of calculating the interest charge on a loan. Simple interest is determined by multiplying the daily interest rate by the principal by the number of days that elapse between payments.


# A = P (1 + rt)
# si= (p*r*t)/100
# A	=	final amount
# P	=	initial principal balance
# r	=	annual interest rate
# t	=	time (in years)


p=int(input(" enter the initial principal balance "))
r=int(input(" enter the annual interest rate "))
t=int(input(" enter the time (in years) "))

si=(p*r*t)/100
A= si+ p

print("the total si of ",t,si) 
print('the total amount has to pay after ',t, A)
