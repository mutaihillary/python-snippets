#def binary_converter(n):
  #  if(n==0):
   #     return "0"
    #elif(n>255):
     #   print("out of range")
      #  return ""
    #else:
     #   ans=""
      #  while(n>0):
       #     temp=n%2
        #    ans=str(temp)+ans
         #   n=n/2
        #return ans

def binary_converter(x):
  if not (isinstance(x, int) and x >= 0 and x <= 255):
    return "Invalid input"
  return bin(x)[2:]