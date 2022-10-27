v=int(input())
k=0
for j in range(1,v//2,1):
    if(v==j*j):
        k=k+1
        break
if k==0:
    print('False')
else:
    print('True')