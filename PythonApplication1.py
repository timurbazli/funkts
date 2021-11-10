from module1 import *

while 1:
    print("Funktsioonid".center(50," "))
    v=input("Arithmetic - A, Is_year_leap - Y, Square - S")
    v=input()

    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    if v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print(rezult)
    if v.upper()=="S":
        rezult=square(int(input("Sisesta ruudu külk: ")))
        print(rezult)