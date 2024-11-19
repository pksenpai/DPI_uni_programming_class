w=float(input("please enter width of your land?"))
h=float(input("please enter height of your land?"))
s=w*h
if s>=300:   
   print("your land is valuable")
   p=float(input("please neter price of each meter?")) 
   k=s*p
   print("value of your land is",k)
else:
   print("not good")