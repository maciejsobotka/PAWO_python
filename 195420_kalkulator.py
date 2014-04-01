#!/usr/bin/python
#-*- coding: utf-8 -*-

# Maciej Sobótka
# 195420

def add(a, b):
    return num(a)+num(b)

def sub(a, b): 
    return num(a)-num(b)

def mult(a, b): 
    return num(a)*num(b)

def div(a, b): 
    return num(a)/num(b)

def num(x):
    """
    Sprawdzenie czy liczba
    """
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return None

def eq_to_string(oper, result):
    """
    Działanie do stringa
    """
    return "{1} {0} {2} = {3}".format(oper[0], oper[1], oper[2], result)

def save(name,eq):
    """
    Zapis działań do pliku
    """
    f = open(name, 'w')
    f.write(eq)
    f.close()

end=False     # bool na koniec prog (koniec dla q)
eq=""         # string na dzialania
while end==False:
    Error=False
    oper = raw_input("Podaj działanie: ")
    oper = oper.split()                # dzielenie po spacjach
    if oper[0]=='q':
        end=True
        print "Zakończenie programu"
    elif "save" in oper[0]:
        try:
            save(oper[1],eq)
        except IndexError:             # jak nie ma nazwy pliku
            print "Za mało argumentów"
    else:
        try:
            if num(oper[1])==None or num(oper[2])==None:
                Error=True             # jak nie liczby
                print "Podano błedne argumenty"
        except IndexError:             # jak za mało argumentów
            Error=True
            print "Za mało argumentów"
        
        if Error==False:               # jak wszystko ok
            if oper[0]=='+':
                result=add(oper[1],oper[2])
                print result
                eq+=eq_to_string(oper, result)+'\n'
            elif oper[0]=='-':
                result=sub(oper[1],oper[2])
                print result
                eq+=eq_to_string(oper, result)+'\n'
            elif oper[0]=='*':
                result=mult(oper[1],oper[2])
                print result
                eq+=eq_to_string(oper, result)+'\n'
            elif oper[0]=='/':
                if oper[1]!='0':
                    result=div(oper[1],oper[2])
                    print result
                    eq+=eq_to_string(oper, result)+'\n'
                else:
                    print "Nie dzielimy przez 0!"
            else:
                print "Błędne działanie"
