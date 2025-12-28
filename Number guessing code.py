import random 

n=random.randint(1,100)
print("Hello there. Welcome to the Number Guessing code.Let us begin.")
flag=False
for i in range (5) :
   num=int(input("Enter a number between 1 to 100 : \n"))
   if(num==n) :
    print("You guessed it right. Well Done!!!!")
    flag=True
    break

   elif abs(num-n)<=2 :
    print("You are too close")

   else :
      if num>n :
         print("Number which you have guessed is very high")
      else :
        print("Number which you have entered is too low");

if(flag==False) :
  print("You Lose.The number is ",n)