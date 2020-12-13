# calling page!
from decimal_to_other import  decimal_to
from other_to_decimal import other_to_decimal
inp = input("what's your Enter number:\n decimal:\n binary:\n octal:\n hexa :")
# decimal to other
if inp == "decimal":
    num =int(input("ENter your number:"))
    con =input("Convert\n binary: \n octal: \n hexa:")
    if con == "binary":
        con = 2
    elif con == "octal":
        con = 8
    elif con =="hexa":
        con = 16
    var = decimal_to(num,con) 
    x = "".join(var)
    print("convert  number:",x)     
# binary to other    
elif inp =="binary":
    num = input("Enter your binary number:")
    con = input("Convert \n decimal: \n octal: \ hexa:")
    lst = list(num)
    if con == "decimal":
        ver = 2
        z = other_to_decimal(lst,ver)
        print(z)
    elif con =="octal":
        ver = 2
        x = other_to_decimal(lst,ver)    
        j = decimal_to(x,8)
        zz ="".join(j)
        print("convert  number:",zz)  
    elif con == "hexa":
        ver =2
        x = other_to_decimal(lst,ver)
        j = decimal_to(x,16)
        zz="".join(j)
        print("convert  number:",zz) 
# octal to other            
elif inp == "octal":
    num = input("Enter your octal number:")
    con = input("Convert \n decimal: \n binary: \n hexa:")
    lst = list(num)
    if con == "decimal":
        ver = 8
        z = other_to_decimal(lst,ver)
        print(z)
    elif con =="binary":
        ver = 8
        x = other_to_decimal(lst,ver)    
        j = decimal_to(x,2)
        zz ="".join(j)
        print(zz)  
    elif con =="hexa":
        ver = 8
        x = other_to_decimal(lst,ver)    
        j = decimal_to(x,16)
        zz ="".join(j)
        print("convert  number:",zz)  
# hexa to other 
elif inp == "hexa":
    num = input("Enter your hexa number:")
    con = input("Convert \n decimal: \n binary: \ octal:")
    lst = list(num)
    if con == "decimal":
        ver = 16
        z = other_to_decimal(lst,ver)
        print(z)
    elif con =="binary":
        ver = 16
        x = other_to_decimal(lst,ver)    
        j = decimal_to(x,2)
        zz ="".join(j)
        print(zz)  
    elif con =="octal":
        ver = 16
        x = other_to_decimal(lst,ver)    
        j = decimal_to(x,8)
        zz ="".join(j)
        print("convert  number:",zz)  
