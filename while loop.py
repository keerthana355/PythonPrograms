#Python program to print numbers from 1 to 10
i=1
while i<=10:
 print(i)
 i=i+1

#Python program to print numbers divisible by 5 and 7 from 1 to 50
a=1
while a<=50:
  if a%5==0 or a%7==0:
   print(a,end=' ')
  a=a+1

#Python program to print multiplication table of given number
a=int(input("Enter the number"))
i=1
while i<11:
 print(a,"x",i,"=",a*i)
 i=i+1

#Python program to calculate the sum of squares of first 15 natural numbers
num=1
sum=0
while num<=15:
 sum=num**2+sum
 num=num+1
print("The sum of the squares is",sum)

#Python program to check the number is prime or not
n=int(input("Enter the number"))
f=0
i=2
while i<=n/2:
 if n%i==0:
  f=1
  break
 i=i+1
if f==0:
 print("The entered number is prime")
else:
 print("The entered number is not prime")

#Python program to check the given number is armstrong number or not
num=int(input("enter thr number:"))
sum=0
temp=num
while temp>0:
 digit=temp%10
 sum+=digit**3
 temp//=10
if num==sum:
 print(num,"is an armstrong number")
else:
 print(num,"is not an armstrong number")
