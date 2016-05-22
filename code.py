n=int(input())
p=1
a=[[0 for s in range(n)] for i in range(n)]
y=0
t=n**2
while p<=t:
    for i in range(y,y+1):
        for j in range(y,n-y):
            a[i][j]=p
            p+=1
    for i in range(y+1,n-y-1):
        for j in range(n-y-1,n-y):
            a[i][j]=p
            p+=1
    for i in range(n-y-1,n-y):
        for j in range(n-y-1,y,-1):
            a[i][j]=p
            p+=1
    for i in range(n-y-1,y,-1):
        for j in range(y,y+1):
            a[i][j]=p
            p+=1
    y+=1
for row in a:
    print('\t'.join([str(elem) for elem in row]))
