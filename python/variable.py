# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%   Variable 







#variable
#function
#object

var1=10
var2=15

gun="pazartesi"  #string

var3=10.0  #double (float)

5var= 10 #ınvalid syntax 

Var7=10 # standart convention of python'a göre buyuk harfle baslamak uygun degil





# %%   String







s="bugun gunlerden pazartesi"

variable_type=type(s)  #str=sring

print(s)

var1="ankara"
var2="ist"
var3=var1+var2

var4="100"
var5="200"
var6=var4+var5

uzunluk=len(var6)




# %%   Numbers






#int double
ineger_deneme= -50

# double= float= ondalikli sayı

float_deneme= -30.7






# %%   Built-in functions


str1="deneme"

float1=10.6

str2="1005"





# %%   User Defined Functions



var1=20
var2=50 
output=((var1+var2)*50)/100.0*var1/var2

var3=40
var4=60

output2=((var3+var4)*50)/100.0*var3/var4

#fonksiyon prametresi = input

def benim_ilk_func(var1,var2):
    
    """ 
    ilk deneme
    parametre:
    return:
        
    """
    
    output=(((var1+var2)*50)/100.0)*var1/var2
    
    return output

sonuc=benim_ilk_func(var1,var2)

def benim_ilk_func(a,b):
    
    """ 
    ilk deneme
    parametre:
    return:
        
    """
    
    output=(((a+b)*50)/100.0)*a/b
    
    return output

def deneme1():
    print("bu benim ikinci denemem")
    
# %%   Default and Flexible Functions


#default f:cemberin cevre uzunlugu

def cember_cevresi_hesapla(r):
    
    """
    cember cevresi Hesapla
    input(parametre)=r
    output=cemberin cevresi 
    """
    
    output=2*3.14*r
    return output 


def cember_cevresi_hesapla(r,pi=3.14):
    
    """
    cember cevresi Hesapla
    input(parametre)=r,pi
    output=cemberin cevresi 
    """
    
    output=2*pi*r
    return output 


#flexible


def hesapla(boy,kilo,*args):
    print(len(args))
    output=boy+kilo
    return output 

def hesapla(boy,kilo,*args):
    print(args)
    output=boy+kilo
    return output 

def hesapla(boy,kilo,*args):
    print(args)
    output=(boy+kilo)*args[0]
    return output 


# def hesapla(boy,kilo,yas):
#     output=(boy+kilo)*yas 
#     return output 


# %%   QUIZ


# int variable yas
# string name sisim
# fonksiyon print(type(),len(), float())
# *args soyisim
# default param etre ayakkabı numarası


yas=10
name="ali"
soyisim="veli"

def function_quiz(yas,name,*args, ayakkabi_numarasi=35,):
    print("Cocugun ismi: ",name,"yasi: ",yas,"ayak numarasi: ", ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    return output 

sonuc=function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)

# %%   Lambda Function



def hesapla(x):
    output=x*x
    return output

sonuc=hesapla(3)

sonuc2= lambda x: x*x
print(sonuc2(3))


# %%   List


var1=10
var2=20
var3=30


liste = [1,2,3,4,5,6]
type(liste)

liste_str =["pazartesi","sali","carsamba"]  
type(liste_str)

value=liste[1]
print(value)

liste_str[1]
liste[4]

last_value=liste[-1]
print(last_value)

liste_divide= liste[0:3]
print(liste_divide)


liste[-1]
liste[0:3]


dir(liste)

liste.append(7)

liste.remove(7)

liste.reverse()


liste2=[1,5,4,3,6,7,2]
liste2.sort()

string_int_liste=[1,2,3,"aa","bb"]

# %%   Tuple


t=(1,2,3,3,4,5,6)


dir(tuple)


t.count(3)
t.index(5)   

# %%   Dictionary


dictionary={"ali":32,"veli": 45, "ayse":13}

# ali,veli,ayse = KEYS
# 32,45,13= VALUES

dictionary.keys()
dictionary.values()

def deneme():
    dictionary={"ali":32,"veli": 45, "ayse":13}
    return dictionary 

dic=deneme()


# %%   Conditionals # if-else Statements


var1=10
var2=20

if(var1>var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var1 esittir var2")
else:
    print("var1 kucuktur var2")
        


liste=[1,2,3,4,5]

if 6 in liste:
    print("evet 6 degeri listenin icinde")
else:
    print("hayır")
    
value=3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayır")


dictionary={"ali":32,"veli": 45, "ayse":13}

keys=dictionary.keys()

if "ali" in keys:
    print("evet")
else:
    print("hayır")
    
# %%   QUIZ 2




# 1639.yıl == 17. yuzyıl 

# metod yazın 
    # input integer yıllar
    # output integer yüzyıl
    # input= year   1<=year<=2005
    
def year2Century(year):
    str_year=str(year)
    if (year<1 or year>2005):
        print("error")
    elif(year<100):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"):
            return int((str_year)[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4]=="00"): 
            return int((str_year)[0:2])
        else:
            return int(str_year[0:2])+1
       
# %%   For Loop




for each in range(1,11):
    print(each) 


for each in "ankara ist":
    print(each)        


for each in "ankara ist".split():
    print(each)
    
liste=[1,4,5,6,8,3,3,4,67]

summation=sum(liste)


count=0
for each in liste:
    count=count+each
    print(count)



# %%   While Loop


liste=[1,4,5,6,8,3,3,4,67]

sinir=len(liste)  
each=0
count=0
while(each<sinir):
    count=count+liste[each]
    each=each+1
count    


i=0
while(i<4):
    print(i)
    i=i+1
    
# %%   QUIZ 3


# listenin içindeki en küçük sayıyı bul for veya while ile

min(list)

liste=[1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

smaller=1000000

for each in liste:
    if(each<smaller):
        smaller=each
    else:
        continue
print(smaller)
        




