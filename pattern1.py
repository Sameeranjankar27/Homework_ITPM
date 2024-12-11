# we will see when i = rows and j= column will be same

# 1. printing * by 4 lines when i==j
n= 4
i=1
while i<=n:
    j=1
    while j<=n:
        print("*",end='')
        j = j+1
    print()
    i = i+1


# 2. printing 1 , 2 , 3 , 4 in pattern 

n= 4
i=1
while i<=n:
    j=1
    while j<=n:
        print(i, end='')
        j = j+1
    print()
    i = i+1

# 3. Printing 1234 by each line till 4th row

n=4
i=1
while i<=n:
    j=1
    while j<=n:
        print(j , end='')
        j=j+1
    print()
    i=i+1



# 4. printing 4321 by each row till 4th row

n=4
i=1
while i<=n:
    j= 1
    while j<=n:
        print(n-j+1, end='')
        j=j+1
    print()
    i=i+1





