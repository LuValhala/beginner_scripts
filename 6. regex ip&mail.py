# -*- coding: utf-8 -*-
"""
Sipmle regional expression search and match excercise. Matching the IP and searching for mail.
Ľuboš Valčo, april 2016
"""
import re
#optionaly: ip=input("Zadajte IP adresu:")
ip = "78.99.245.194"
findip=re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)
if findip:
    print(ip)
mail = "contact us at info@gmail.com for further help, this is rather our false page not@an_email"
findmail=re.search(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)",mail)
if findmail:
    print (findmail.group())
