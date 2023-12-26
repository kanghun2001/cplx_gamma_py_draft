import math
def gamma(a, b, N, M):
    try:
        if 1<=a<=2:
            sum = 0
            while(True):
                n = 0
                tmp = (N+1)^n
                for k in range(0, n+1):
                    tmp = tmp / (complex(a+k, b))
                
                if abs(tmp * math.exp(M*math.log(2))) < 1:
                    break
                else:
                    sum = sum + tmp
                    n = n + 1
            sum = sum * math.exp(-N-1)*complex(math.cos(b*math.log(N+1)), math.sin(b*math.log(N+1)))
            sum = sum * math.exp(a*math.log(N+1))       
            return sum
        elif a < 1:
            a1 = a
            count = 0
            while(True):
                if 1<=a1<=2:
                    break
                a1 = a1 + 1
                count = count + 1
                
            temp = gamma(a1, b, N, M)
            for k in range(0, count):
                temp = temp / complex(a1-1, b)
                a1 = a1 - 1
            return temp
        else:
            a1 = a
            count = 0
            while(True):
                if 1<=a1<=2:
                    break
                a1 = a1 - 1
                count = count + 1
            temp = gamma(a1, b, N, M)
            for k in range(0, count):
                temp = temp * complex(a1, b)
                a1 = a1 - 1
            return temp
    except ZeroDivisionError as e:
        return "undefined"
    
print(gamma(0, 1, 6, 14))
    





