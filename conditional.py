#  print Word of number
# n=int(input("Enter a Number"))
# if(n ==1):
#     print("One")
# if(n ==2):
#     print("Two")
# if(n ==3):
#     print("Three")
# if(n ==4):
#     print("Four")
# if(n ==5):
#     print("Five")
# if(n>5 or n<1):
#     print("Invalid Number")  



# # program for driver selection
# name=input("Enter your name")
# age=int(input("Enter your age"))
# ms=input("Enter merrital status")
# if(name =="Rajesh"):
#     if(age>18 and age<50):
#         if(ms =='m'):
#            print("You are selected.....")


# Program for number even or odd
# n=int(input("Enter a number"))
# if(n%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")    


# Program for number +ve or -ve
# n=int(input("Enter a number"))
# if(n>=0):
#     print("Number is +ve")
# else:
#     print("Number is -ve")    

# Grater between two number.
# a=int(input("Enter First Number"))
# b=int(input("Enter Second Number"))
# if(a>b):
#     print("Grater number is %d" %(a))
# else:
#     print("Grater number is %d" %(b))    

# # Grater between Three numbers.
# a=int(input("Enter First Number"))
# b=int(input("Enter Second Number"))
# c=int(input("Enter Third Number"))
# if(a>b and a>c):
#     print("Grater is number %d" %(a))
# elif(b>c):
#     print("Grater is number %d" %(b))
# else:
#     print("Grater is number %d" %(c))      

# n=int(input("Enter the limit"))
# i=1 # intilization
# while(i<=n):
#     print(i*i,end=" ")
#     i=i+1
#  wap to find table of numbers.
# n=int(input("Enter a number"))
# i=1
# while(i<=10):
#     print(n*i,end=" ")
#     i=i+1


# n=int(input("Enter the limit"))
# i=1 #initilization
# sum=0
# while(i<=n): # condition
#     print(i)
#     sum+=i
#     i=i+1 # increment
# print("Total is:",sum)    

# Fibbonacci Series.
# 0 1 1 2 3 5 8 13 21 34 ....n
# n=int(input("Enter the limit"))
# a=0
# b=1
# if(n ==1):
#     print(a,end=" ")
# if(n ==2):
#     print(a,end=" ")
#     print(b,end=" ")   
# if(n>2):
#     print(a,end=" ")
#     print(b,end=" ")   
#     i=1
#     while(i<=n-2):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
#         i=i+1

# Factorial of numbers
# n=int(input("Enter the number"))
# f=1
# while(n!=0):
#     f=f*n
#     n=n-1
# print("factorial is:",f)

# # Number Parlindrome or not
# n=int(input("Enter a number"))
# m=n
# s=0
# while(n!=0):
#     r=n%10
#     s=s*10+r
#     n=n//10
# #print("Reverse is:",s)    
# print("Number is palindrome") if(m==s) else print("Number is not parlindrome")

# Armstrong Number or not

# n=int(input("Enter a Number"))
# m=n
# s=0
# while(n!=0):
#     r=n%10
#     s=s+(r*r*r)
#     n=n//10
# print("Number is Armstrong") if(m==s) else print("Number is not Armstrong")   


# n=int(input("Enter a Number"))
# s=0
# while(n!=0):
#     r=n%10
#     s=s*10+r
#     n=n//10
       
# while(s!=0):
#     r=s%10
#     print(r)
#     s=s//10    

# # How to print word format of number
# n=int(input("Enter a number"))
# s=0
# while(n!=0):
#     r=n%10
#     s=s*10+r
#     n=n//10

# while(s!=0):
#     r=s%10
#     if(r==0):
#         print("Zero",end="")
#     elif(r==1):
#         print("One",end="")    
#     elif(r==2):
#         print("Two",end="")  
#     elif(r==3):
#         print("Three",end="")
#     elif(r==4):
#         print("Four",end="")
#     elif(r==5):
#         print("Five",end="")
#     elif(r==6):
#         print("Six",end="")
#     elif(r==7):
#         print("Seven",end="")
#     elif(r==8):
#         print("Eight",end="")
#     elif(r==9):
#         print("Nine",end="")
#     s=s//10                                   

# # Python Project Password Generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(',')' '*', '+']
# print("Welcome to Password Generator!")
# n_letters=int(input("How many letters you want in your password?\n"))
# n_symbols=int(input("How many symbols you want in your password?\n"))
# n_numbers=int(input("How many numbers you want in your password?\n"))
# password=""
# for i in range (1,n_letters+1):
#     char= random.choice(letters)
#     password += char 
# for i in range (1,n_symbols+1):
#     char= random.choice(symbols) 
#     password += char
# for i in range (1,n_numbers+1):
#     char= random.choice(numbers)
#     password += char
# print(password)         



