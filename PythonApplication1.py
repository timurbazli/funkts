from module1 import *

while 1:
    print("Funktsioonid".center(50," "))
    v=input("Arithmetic - A\nIs_year_leap - Y\nSquare - S\nSeason - M\nBank - B\nIs_prime - I\nXor_cipher - X\nDate - D")
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
        sqr=(float(input("Sisesta ruudu külk: ")))
        rezult=square(sqr)
        print(rezult)
    if v.upper()=="M":
        rezult=season(int(input("Sisesta kuu: ")))
        print(rezult)
    if v.upper()=="B":
        summa=(float(input("Sisesta raha: ")))
        years=(int(input("Sisesta aasta: ")))
        rezult=bank(summa, years)
        print(f"Вы получите {rezult} за {years} years.")
    if v.upper()=="I":
        rezult=is_prime(float(input("Sisesta number: ")))
        print(rezult)
    if v.upper()=="X":
        print("Kodeerimine".center(60,"*"))
        rezult=xor_cipher(input("Sisesta text: "), input("Sisesta võti: "))
        print(rezult)
        print("Dekodeerimine".center(60,"*"))
        de_rezult=xor_cipher(rezult, input("Sisesta võti: "))
        print(de_rezult)
    if v.upper()=="D":
        day=int(input("Sisesta päev:"))
        month=int(input("Sisesta month:"))
        year=int(input("Sisesta year:"))
        rezult=date(day, month, year)
        print(rezult)