# First N natural Numbers

n = int(input("Enter the n:"))
for i in range ( 1,n+1):
    print(i)


# First N even Natural numbers

n = int(input("Enter the n:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

# First N odd Natural numbers
n = int(input("Enter the n:"))
for i in range(1,n+1):
    if i%2==0:
        pass
    else:
        print(i)

# First N Multiple of 3
n = int(input("Enter the n:"))
for i in range (1,n+1):
    print(3*i)

# First N multiple of 5
n = int(input("Enter the n:"))
for i in range(1,n+1):
    print(5*i)
# Multiple of 2 Till N
n = int(input("Enter the n:"))
for i in range (1,n+1):
    print(2*i)

# Multiple of 2 or 3 Till N
n = int(input("Enter the n:"))
for i in range (1,n+1):
    if i%2==0 or i%3==0:
        print(i)

# Multiple of 2,5 or 7 Till N
n = int(input("Enter the n:"))
for i in range (1,n+1):
    if i%2==0 or i%5==0  or i%5==0:
        print(i)
        
# First N numbers of 3,5 or 7
n = int(input("Enter the n:"))
for i in range ( 1,n+1):
    if i%3==0 or i%5==0 or i%7==0:
        print(i)


