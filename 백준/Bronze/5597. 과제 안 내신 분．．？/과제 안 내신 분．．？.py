a = [0]*30
for i in range(28):
    b = int( input() )
    a[b-1] = 1
for i in range( len(a) ):
    if(a[i]==0):
        print(i+1)