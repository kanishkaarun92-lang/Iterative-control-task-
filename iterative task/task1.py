
# sum of digits
n=int(input("enter a number:"))
sum = 0
while n >0:
    digit = n% 10
    sum = sum + digit
    n = n // 10
print(sum)

#count number of digits
n = int(input("enter a number:"))
count =0
while n >0:
    n=n//10
    count = count +1
print(count)

# find factors
a = int(input("enter a number:"))
for i in range(1,a+1):
    if a % i ==0:
        print(i)
# count factors
a = int(input("enter a number:"))
count = 0
for i in range(1,a+1):
    if a % i ==0:
        count = count + 1
print(count)

# prime number check
a = int(input("enter a  number:"))
count = 0
for i  in range(1,a+1):
    if a%i==0:
        count = count + 1
if count == 2:
    print("it is prime")
else:
    print("it is not prime")
    
#greatest common factor (gcf/gcd)
n=int(input("enter a number1:"))
a=int(input("enter a number2:"))
gcf = 1
for i in range(1,min(n,a)+1):
    if n %i==0 or a%i==0:
        gcf = i
print(gcf)

# common factor 
n=int(input("enter a number1:"))
m=int(input("enter a number2:"))
for i in range(1,min(n,m)+1):
    if n %i==0 or m%i==0:
        print(i)

#fibnoacci series
a=0
b=1
while a <=50:
    print(a)
    c = a+ b
    a=b
    b=c
    
# factorial calculation
n = int(input("enter a number:"))
c=1
for i in range(1,n+1):
    c = c * i
print(c)

#sum of even and odd numbers

n=int(input("enetr a number:"))
even_sum = 0
odd_sum =0
for i in range(1,n+1):
    if i%2==0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum +i
        
print("even_sum:",even_sum)
print("odd_sum:",odd_sum)

# palindrome number
n = int(input("enter a number:"))
original = n
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse * 10 + digit
    n= n//10
if original == reverse:
    print("it is palindrome")
else:
    print("it is palindrom")

# pattern printing
for i in range(1,6):
    for j in range(i): 
        print("*",end ="")
    print()
# patter printing in number pyramid

for i in range(1,6):
    for j in range(1,i+1): 
        print(i,end ="")
    print()

for i in range(1,6):
    for j in range(1,i+1): 
        print(j
              ,end ="")
    print()
