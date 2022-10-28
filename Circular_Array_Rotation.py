N,rot,n=map(int,input().split())
vk=list(map(int,input().split()))
for _ in range(rot):
    t=vk[-1]
    for r in range(len(vk)-1,0,-1):
        vk[r]=vk[r-1]
    vk[0]=t
for _ in range(n):
    print(vk[int(input())])