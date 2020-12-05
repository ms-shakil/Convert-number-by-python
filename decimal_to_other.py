# That functon work for number convert decimal to other number:
import math
def decimal_to (number,convert):
    lst = []
    while number >0:
        mod = number % convert
        mod = math.floor(mod)
        if mod == 10:
            mod = "A" 
        elif mod == 11:
            mod ="B"
        elif mod == 12:
            mod = "C"
        elif mod == 13:
            mod = "D"
        elif mod == 14:
            mod = "E"
        elif mod == 15:
            mod = "F"
        else:
            mod = mod
        mod = str(mod)
        lst.append(mod)
        if mod == "A":
            mod = 10
        elif mod == "B":
            mod =11
        elif mod == "C":
            mod = 12
        elif mod == "D":
            mod = 13
        elif mod == "E":
            mod = 14
        elif mod == "F":
            mod = 15
        else:
            mod = mod
        mod = int(mod)
        num = number - mod
        div = num / convert
        number = div
    lst.reverse()
    return lst

