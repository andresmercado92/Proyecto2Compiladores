cad="baab"
"""a,b=cad.split("c")
c=b[::-1]
if(a==c):
	print("c mamo")
print(a)
print(b)
print(c)"""

mitad=int(len(cad)/2)
if(len(cad) % 2 == 0):
	cad1=cad[:mitad]
	cad2=cad[mitad:]
	if(cad1==cad2[::-1]):
		print("c mamut")