from math import *
from random import *

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
    :rtype var: Märamata tüüb
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
            r="Div/0"
    else:
        r="Tundmatu sym"
        r=0.0
    return r

def is_year_leap(year: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus logilises formaadis
    Kirjuame suvalise aasta ja programm määrab ära, kas viisaasta või liifaasta
    """
    if year%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(s1:float):
    """Программа принимает 1 сторону квадрата, при нахождении площади (S=a*a,), при нахождении пириметра (P=a*4), а диагональ мы находим при помощи теоремы Пифагора.
    otv - переменная, которую я сделал для return
    """
    if s1!=0:
#        otv=""
        p=s1*4
        s=s1*s1
        d=sqrt(s1*s1+s1*s1)
        r=(p,s,d)

#        print("P=", p)
#        print("S=", s)
#        print("d=", d)
    return r

def season(kuu:int):

    """
Программа принимает 
:param int kuu: kuu jarjekordne number
:rtype str: hooja nimetus
    """
    if kuu== 12 or 1 <= kuu <=2:        #Если месяц 12,1,2 - то это зима
        vd="See on talv"
    elif 3 <= kuu <= 5:        #Если месяц 3,4,5 - то это весна
        vd="See on kevad"
    elif 6 <= kuu <= 8:        #Если месяц 6,7,8 - то это лето
        vd="See on suvi"
    elif 9 <= kuu <= 11:        #Если месяц 9,10,11 - то это осень
        vd="See on sügi"
    else:
        vd="Viga!"              #Если это любое другое число - то это ошибка.
    return vd

def is_prime(numb:float):
    if numb==0:         #Если число 0, то ошибка
        vdl="Viga"
    elif numb%numb==0:     #Если число делится само на себя без остатка, то True, если нет, то False
        vdl=True
    else:               
        vdl=False
    return vdl

def xor_cipher(string:str, key:str)->str:
    rezult=""
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp^=ord(key[j])       #ord - десятичное число, которое кодируется в букву. 
        rezult +=chr(temp)
    return rezult


def  XOR_uncipher(string:str, key:str)->str:
    """Tavaline sõna kodeeritakse
    """
    rezult=""
    temp= []
    for i in range (len(string)):
        temp.append(string[i]) # Näitab kood 
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j])^ ord(temp[i]))    #chr - наоборот берёт число и возвращает букву.
        rezult+=temp[i]
    return rezult

def bank(summa:float, years:int):
    if summa>=0:
        procenti=years*1.1
        proc=summa*procenti
    return proc

def date(day:int, month: int, year: int):
    if year%4==0 and day ==29:
        if ((month>=1) and (month<=12)) and (day<=31 or day==31) and year >0:
                otvet=True
    else: 
        otvet=False
    return otvet
        


#:rtype bool: - значение или True или False