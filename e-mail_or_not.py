# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:52:20 2023

@author: Ashleroa
"""

def eposta_kontrol():
    girdi = input("Gecerli bir e posta adresi giriniz:")
    
    while not (("." in girdi) and ("@" in girdi)):
        print("Üzgünüm bu e-posta adresi gecerli degil...")
        girdi = input("Gecerli bir e posta adresi giriniz:")
    
    else:
        print("Tebrikler e-posta adresiniz dogru!")
    
eposta_kontrol()





