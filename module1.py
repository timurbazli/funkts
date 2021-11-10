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
    p=s1*4
    s=s1*s1
    d=(s1**2) + (s1**2)
    print("P=", p)
    print("S=", s)
    print("d=", d)   