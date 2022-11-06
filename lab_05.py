# Python3 program to find the smallest
# twin in given range
import random
 
# Iterative Function to calculate
# (a^n)%p in O(logy)
def power(a, n, p):
     
    # Initialize result
    res = 1
     
    # Update 'a' if 'a' >= p
    a = a % p 
     
    while n > 0:
         
        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n must be even now
            n = n // 2
             
    return res % p
     
# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def isPrime(n, k):
     
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    # Try k times
    else:
        for i in range(k):
             
            # Pick a random number
            # in [2..n-2]     
            # Above corner cases make
            # sure that n > 4
            a = random.randint(2, n - 2)
             
            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False
                 
    return True
             
# Driver code
k = 3
if isPrime(11, k):
  print("true")
else:
  print("false")
   
if isPrime(15, k):
  print("true")
else:
  print("false")
 
# This code is contributed by Aanchal Tiwari





# Python3 program Miller-Rabin primality test
import random
 
# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
     
    # Initialize result
    res = 1;
     
    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;
 
# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
     
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);
 
    # Compute a^d % n
    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    # Return composite
    return False;
 
# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime( n, k):
     
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Iterate given number of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;
 
# Driver Code
# Number of iterations
k = 4;
 
print("All primes smaller than 100: ");
for n in range(1,100):
    if (isPrime(n, k)):
        print(n , end=" ");
 
# This code is contributed by mits




# Python3 program to implement Solovay-Strassen
# Primality Test
import random

# modulo function to perform binary
# exponentiation
def modulo(base, exponent, mod):
	x = 1;
	y = base;
	while (exponent > 0):
		if (exponent % 2 == 1):
			x = (x * y) % mod;

		y = (y * y) % mod;
		exponent = exponent // 2;

	return x % mod;

# To calculate Jacobian symbol of a
# given number
def calculateJacobian(a, n):

	if (a == 0):
		return 0;# (0/n) = 0

	ans = 1;
	if (a < 0):
		
		# (a/n) = (-a/n)*(-1/n)
		a = -a;
		if (n % 4 == 3):
		
			# (-1/n) = -1 if n = 3 (mod 4)
			ans = -ans;

	if (a == 1):
		return ans; # (1/n) = 1

	while (a):
		if (a < 0):
			
			# (a/n) = (-a/n)*(-1/n)
			a = -a;
			if (n % 4 == 3):
				
				# (-1/n) = -1 if n = 3 (mod 4)
				ans = -ans;

		while (a % 2 == 0):
			a = a // 2;
			if (n % 8 == 3 or n % 8 == 5):
				ans = -ans;

		# swap
		a, n = n, a;

		if (a % 4 == 3 and n % 4 == 3):
			ans = -ans;
		a = a % n;

		if (a > n // 2):
			a = a - n;

	if (n == 1):
		return ans;

	return 0;

# To perform the Solovay- Strassen
# Primality Test
def solovoyStrassen(p, iterations):

	if (p < 2):
		return False;
	if (p != 2 and p % 2 == 0):
		return False;

	for i in range(iterations):
		
		# Generate a random number a
		a = random.randrange(p - 1) + 1;
		jacobian = (p + calculateJacobian(a, p)) % p;
		mod = modulo(a, (p - 1) / 2, p);

		if (jacobian == 0 or mod != jacobian):
			return False;

	return True;

# Driver Code
iterations = 50;
num1 = 15;
num2 = 13;

if (solovoyStrassen(num1, iterations)):
	print(num1, "is prime ");
else:
	print(num1, "is composite");

if (solovoyStrassen(num2, iterations)):
	print(num2, "is prime");
else:
	print(num2, "is composite");

# This code is contributed by mits
