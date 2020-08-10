import math

k=(float(1*10**14))

z=(float(75*10**3))
print(z)
x=(float(8.314*300.15))
print(x)

e1=(z/x)
print(e1)

e2=math.exp(e1)


final=k-e2
print(final)
