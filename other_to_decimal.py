# That function work for convert number other to decimal:
def other_to_decimal(lst,convert):
     lst2 =[]
     for i in lst:
          j =0
          if i =="A":
               i =10
          elif i =="B":
               i =11
          elif i == "C":
               i = 12
          elif i == "D":
               i=13
          elif i == "E":
               i = 14 
          elif i =="F":
               i =15
          j= int(i)
          lst2.append(j)
     data = []
     for i in range(1,len(lst2)+1,1):
          dec =lst2[i*-1]*convert**(i-1)
          data.append(dec)

     e = 0
     for i in data:
          e+=i
     return e
