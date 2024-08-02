year= int(input(" enter year :"));
#print(type(year))
"""
if(year%400==0):
    print(year,"= Leap Year")
elif (year%100!=0 and year%4==0):
    print(year,"= Leap Year")
else:
    print(year,"= Not Leap Year")
"""

if(year%400==0 or (year%100!=0 and year%4==0)):
    print(year,"= Leap Year")
else:
    print(year,"= Not Leap Year")
    
    
