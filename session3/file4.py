x = input("please neter your password?")

if len(x) >= 4 and len(x) <= 8 and not ("a" in x):
   print("correct")
else:
   print("wrong")
