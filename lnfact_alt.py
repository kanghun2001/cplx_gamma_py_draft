import math
def lnfact(a, b, l):
	try:		
		sum = math.log(l)*complex(a, b)
		for n in range(1, l+1):
			p = math.log((1+a/n)*(1+a/n)+b/n*b/n)/2
			try:
				q = math.atan(b/(n+a))
			except ZeroDivisionError as e:
				q = math.pi/2*abs(b)/b
			p = complex(p, q)
			sum = sum - p
		return sum
	except ValueError as e:
		return "undefined"
	
nem = complex(input("Enter complex number: "))
re = nem.real
im = nem.imag
inp = int(input("Enter precision parameter: ideally infinity "))
print(lnfact(re, im, inp))

    	    
    	
