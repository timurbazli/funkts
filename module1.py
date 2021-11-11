from math import *

def arithmetic(a: float, b: float, c:str):
    """Lihtne kalkulaator
    + liitmine
    - lahutamine
    * korrutamine
    / jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehnig
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
#            r=var 
            r=0.0
    else:
        print("Viga")
        r=0.0
    return r

def is_year_leap(year: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus logilises formaadis
    """
    if year%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(s1:float):
    if s1!=0:
        otv=""
        p=s1*4
        s=s1*s1
        d=sqrt(s1*s1+s1*s1)
        print("P=", p)
        print("S=", s)
        print("d=", d)
    return otv

def season(kuu:int):

    """
    ord - десятичное число, которое кодируется в букву. 
    chr - наборот берёт число и возвращает букву.
    """
    if kuu== 12 or 1 <= kuu <=2:
        vd="See on talv"
    elif 3 <= kuu <= 5:
        vd="See on kevad"
    elif 6 <= kuu <= 8:
        vd="See on suvi"
    elif 9 <= kuu <= 11:
        vd="See on sügi"
    else:
        vd="Viga!"
    return vd

#def bank(ban:float):
#    if ban==0:
#        total="Viga!"
#    elif ban*1.1:



#    ord - десятичное число, которое кодируется в букву. 
#    chr - наборот берёт число и возвращает букву.
