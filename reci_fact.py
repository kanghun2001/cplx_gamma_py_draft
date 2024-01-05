import math
def lnfact(a, b, s, l):
	try: 
		minuseuler = math.gamma(s) - 1/s
		sum = minuseuler*complex(a, b)
		for n in range(1, l+1):
			sum = sum + complex(a/n, b/n)
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

def reci_fact(a, b, s, l):
	tmp = lnfact(a, b, s, l)
	if tmp == "undefined":
		return 0
	else:
		p = tmp.real
		q = tmp.imag
		p = math.exp(-p)
		r = p*math.cos(q)
		i = -p*math.sin(q)
		return complex(r, i)

nem = complex(input("Enter complex number: "))
re = nem.real
im = nem.imag
zuro, inp = input("Enter two precision parameters: former ideally zero, latter ideally infinity: ").split(" ")
zuro = float(zuro)
inp = int(inp)
print(reci_fact(re, im, zuro, inp))



    	    
    	