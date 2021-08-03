import math
a = float(input("Adicione um número para A  "))
b = float(input("Adicione um número para B  "))
c = float(input("Adicione um número para C  "))

delta = b**2 - 4*a*c

if delta == 0:
   r1 =(-b + math.sqrt(delta))/(2*a)
   r2 =(-b - math.sqrt(delta))/(2*a)
   print("Possui uma raiz real total", r1),
else:
   if delta < 0:
    print("Esta equação não possui raizes reais")
   else:
    r1 =(-b + math.sqrt(delta))/(2*a)
    r2 =(-b - math.sqrt(delta))/(2*a)
    print("Possui duas raizes reais", r1 ,"e", r2)