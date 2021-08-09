  
import math

def delta(a,b,c):
        return b**2 - 4*a*c

def main():
    a = float(input("Adicione um número para A  "))
    b = float(input("Adicione um número para B  "))
    c = float(input("Adicione um número para C  "))
    imprime_raizes(a,b,c) 

def imprime_raizes(a,b,c):
    d=delta(a,b,c)
    if d == 0:
           r1 =(-b + math.sqrt(d))/(2*a)
           print("Possui uma raiz real total", r1),
    else:
           if d < 0:
                    print("Esta equação não possui raizes reais")
           else:
                    r1 =(-b + math.sqrt(d))/(2*a)
                    r2 =(-b - math.sqrt(d))/(2*a)
                    print("Possui duas raizes reais", r1 ,"e", r2)
