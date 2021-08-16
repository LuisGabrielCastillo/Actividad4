import math
def main():
     #escribe tu código abajo de esta línea
     la=float(input("Ingrese lado a "))
     lb=float(input("Ingrese lado b "))
     lc=float(input("Ingrese lado c "))
     s=(lb+la+lc)/2
     from math import sqrt
     area=sqrt(s*(s-la)*(s-lb)*(s-lc))
     print("El área del triangulo es:",area)


if __name__ == '__main__':
    main()
