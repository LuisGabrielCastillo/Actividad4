import math
def main():
     #escribe tu código abajo de esta línea
      la=float(input("Dame el valor a "))
     lb=float(input("Dame el valor b "))
     lc=float(input("Dame el valor c "))
     s=(lb+la+lc)/2
     from math import sqrt
     area=sqrt((s-la)*(s-lb)*(s-lc))
     print("Area:",area)


if __name__ == '__main__':
    main()
