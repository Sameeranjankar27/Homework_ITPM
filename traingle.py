# right angle traingle

i=1
while i<=6:
    j=1
    while j<=6:
        if j<=i:
            print("*",end='')
        j=j+1
    print()
    i=i+1

#####################################################################################
print()
# left side left angle traingle

i=1
while i<=6:
    j=6
    while j>=1:
        if j <=i:
            print("*",end='')
        else:
            print(" ",end ='')
        j=j-1
    print()
    i=i+1

##############################################################################################
print()
# left hand reverse traingle

i=6
while i >=1:
    j=6
    while j>=1:
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
        j=j-1
    print()
    i=i-1

##############################################################################################
print()
# right angle traingle reverse

i=6
while i>=1:
    j=1
    while j<=6:
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
        j=j+1
    print()
    i=i-1


##########################################################################
print()
# Equilatrel traingle 


i=1
while i<=6:
    j=6
    while j>i:
        print(" ",end='')
        j=j-1
    k=1
    while k<=(i*2-1):
        print("*",end='')
        k=k+1
    print()
    i=i+1
##########################################################################################
print()
# reverse traingle

i=6
while i>=1:
    j=6
    while j>i:
        print(" ",end='')
        j=j-1
    k=1
    while k<=(i*2-1):
        print("*",end='')
        k=k+1
    print()
    i=i-1
###########################################################################################
print()


# diamond pattern 

i=1
while i<=6:
    j=6
    while j>i:
        print(" ",end='')
        j=j-1
    k=1
    while k<=(i*2-1):
        print("*",end='')
        k=k+1
    print()
    i=i+1

i=5
while i>=1:
    j=6
    while j>i:
        print(" ",end='')
        j=j-1
    k=1
    while k<=(i*2-1):
        print("*",end='')
        k=k+1
    print()
    i=i-1