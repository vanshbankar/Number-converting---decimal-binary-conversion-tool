"THIS IS TOOL ,WHICH ARE HELPS TO CONVERT BINARY INTO DECIMAL AND DECIMAL INTO BINARY"
print("-"*80)
print("""
  THIS IS TOOL MADE BY VANSHKUMAR BANKAR
  WHICH ARE HELPS TO CONVERT
1.DECIMAL TO BINARY
2.BIANRY TO DECIMAL
3.EXIT

"""
     )
print("-"*80)

userinput=input("Enter Do YOU Want 1 or 2 : ")

while True:
  
  if userinput=="1":
  
    while True:

      quotient=int(input("Enter The Number Do You Want to Binary of These: "))
      reminder=""
      while True:
        if quotient==0:
          reminder=reminder+"0"
          break
        elif quotient==1:
          reminder=reminder+"1"
          break
        else:
          reminder=reminder+str(quotient%2)
          quotient=quotient//2

      print(f"The Binary Of Your number:{quotient} is=",reminder[::-1])
      user=input("Do you want more Binary??(y/n): ").lower()
      if user=="n":
        break
    break
        
  elif userinput=="2":
    binary=input("Enter The Binary Number Do You Want To Its Decimal Number")
    decimal=0
    power=1
    num=["0","1","2","3","4","5","6","7","8","9"]
   
    try:
      for i in binary:
        # try:
        #   if i not in num:
        #     raise ValueError()
        # except ValueError:
        #   print("BINARY CONTAINS ONLY VALUE IN 0 OR 1")
          
        if int(i)>1 or i not in num:
          raise ValueError("Binary only The Numbers of 0 Or 1\nso Enter The Number In The Form of 0 or 1")
        
    except ValueError:
      print("BINARY CONTAINS ONLY VALUE IN 0 OR 1")
    
    else:
      for i in binary:
        decimal+=int(i)*2**(len(binary)-power)
        if power==len(binary):
          break
        power+=1
      print(f"The decimal of Your Binary number {binary} is: ",decimal)
      user=input("Do you want more Binary??(y/n): ").lower()
      if user=="n":
        break
    break 
    
  else:
    break
