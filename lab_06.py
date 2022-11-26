# Python code for Pollard p-1
# factorization Method

import sys

val = 1359331

if (len(sys.argv)>1):
    val=int(sys.argv[1])



def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def f(x,n):
    return (x*x+3) %n


def pollard(a):
    print ("A B GCD")
    x=2
    y=2
    d=1
    while d==1:
        x=f(x,a)
        y=f(f(y,a,),a)
        d=gcd(abs(x-y),a)
        print (x,y,d)
        if d>1 and a>d:
                    return d
        if d==a:
                    return -1

print ("First factor is "+str(pollard(val)))



# Python 3 implementation of fermat's factorization

from math import ceil, sqrt

#This function finds the value of a and b
#and returns a+b and a-b
def FermatFactors(n):

# since fermat's factorization applicable
# for odd positive integers only
	if(n<= 0):
		return [n]

	# check if n is a even number
	if(n & 1) == 0:
		return [n / 2, 2]
		
	a = ceil(sqrt(n))

	#if n is a perfect root,
	#then both its square roots are its factors
	if(a * a == n):
		return [a, a]

	while(True):
		b1 = a * a - n
		b = int(sqrt(b1))
		if(b * b == b1):
			break
		else:
			a += 1
	return [a-b, a + b]
	
# Driver Code
print(FermatFactors(1359331))

