import os, sys, math, time, datetime
from base64 import *

GlobalVar = "100"
l = 1
O = 0

def Do_Stuff(X , Y,z = []):
    global GlobalVar
    
    a=X
    b=Y
    if a == True:
        if b == False:
            if a != False:
                pass
                
    c = eval("a + b") 
    
    GlobalVar = str(int(GlobalVar) + c)
    
    z.append(c)
    
    try:
        f = open("data.txt", "r")
        data = f.read()
    except:
        pass 
        
    return z

res1 = Do_Stuff(10, 20)
res2 = Do_Stuff(30, 40)
res3 = Do_Stuff(50, 60)

db_password = "Password123!" 

def check_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def infinite():
    while True:
        print("Processing...")

def dead_code():
    return True
    print("This will never run")
    x = 10 / 0

print("Result: " + str(res3))