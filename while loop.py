          Program-1
#Python program to print numbers from 1 to 10
i=1
while i<=10:
 print(i)
 i=i+1

'''Output:
1
2
3
4
5
6
7
8
9
10'''
           Program-2
#Python program to print numbers divisible by 5 and 7 from 1 to 50
a=1
while a<=50:
  if a%5==0 or a%7==0:
   print(a,end=' ')
  a=a+1

'''Output:
5 7 10 14 15 20 21 25 28 30 35 40 42 45 49 50'''

            Program-3
#Python program to print multiplication table of given number
a=int(input("Enter the number:"))
i=1
while i<11:
 print(a,"x",i,"=",a*i)
 i=i+1

'''Output:
Enter the number:4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40'''

          Program-5
#Python program to calculate the sum of squares of first 15 natural numbers
num=1
sum=0
while num<=15:
 sum=num**2+sum
 num=num+1
print("The sum of the squares is",sum)

'''Output:
The sum of the squares is 1240'''

           Program-6
#Python program to check the number is prime or not
n=int(input("Enter the number:"))
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

'''Output:
Enter the number:4
The entered number is not prime'''

           Program-7
#Python program to check the given number is armstrong number or not
num=int(input("enter the number:"))
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

'''Output:
enter the number:
153 is an armstrong number'''
