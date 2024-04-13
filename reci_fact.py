import math
def lnfact(a, b, l):
	try: 
		minuseuler = math.log(l)
		sum = minuseuler*complex(a, b)
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

def reci_fact(a, b, l):
	tmp = lnfact(a, b, l)
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
inp = input("Enter precision parameter: ideally infinity: ")
inp = int(inp)
print(lnfact(re, im, inp))



    	    
    	
