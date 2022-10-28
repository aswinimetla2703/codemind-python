vk=int(input())
l=0
for r in range(1,vk+1):
    if vk%r==0:
        l+=1
if l==2:
    print('prime')
else:
    print('not a prime')