#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:13:49 2022

@author: mkc
"""

# Class Constructor
class calisan:
    zam_orani=1.8
    counter=0
    def __init__(self,isim,soyisim,maas): #constructor
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@asd.com"
        calisan.counter=calisan.counter+1
    
    def giveNameSurname(self):
        return self.isim  +" "+self.soyisim
    def zam_yap(self):
        self.maas=self.maas+self.maas*self.zam_orani
        
# calisan1=calisan("ali","aydin",500)
# print(calisan1.maas)
# print(calisan1.giveNameSurname())


#   Class Variable


calisan1=calisan("ali","aydin",100)

print("ilk maas:",calisan1.maas)
calisan1.zam_yap()
print("zamli maas:",calisan1.maas)

calisan2=calisan("ayse","son",200)
calisan3=calisan("ahmet","ilk",600)
calisan4=calisan("hasan","orta",500)

#   Class example

liste=[calisan1,calisan2,calisan3,calisan4]

maxi_maas=-1
top_maas=0
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas=each.maas
        top_maas=each
print(maxi_maas)
print(top_maas.giveNameSurname())



