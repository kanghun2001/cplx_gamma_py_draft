import math
def lnfact(a, b, s, l):
	try: 
		minuseuler = math.gamma(s) - 1/s
		sum = minuseuler*complex(a, b)
		for n in range(1, l+1):
			sum = sum + complex(a/n, b/n)
			p = math.log((1+a/n)*(1+a/n)+b/n*b/n)/2
			q = math.atan(b/(n+a))
			p = complex(p, q)
			sum = sum - p
		return sum
	except ZeroDivisionError as e:
		return "undefined"
	
nem = complex(input("Enter complex number: "))
re = nem.real
im = nem.imag
zuro, inp = input("Enter two precision parameters: former ideally zero, latter ideally infinity: ").split(" ")
zuro = float(zuro)
inp = int(inp)
print(lnfact(re, im, zuro, inp))
	

    	    
    	
