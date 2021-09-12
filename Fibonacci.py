# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:01:37 2021

@author: Suvarna
"""

limit=int(input("Enter the limit:"))
old=0
new=1
fibo=0
print("The Fibonacci Series:",old,new, end =" ")
for i in range (1,limit+1,1):
    fibo=old+new
    print(fibo, end =" ")
    old=new
    new=fibo
