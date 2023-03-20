n=int(input())
arr=list(map(int,input().split()))
flag=false
ans=[]
for i in arr:
    if arr.count(i) > 1 and i not in ans:
        flag=true
        ans.append(i)
if len(ans)>0:
     print(*ans)
else:
     print("no elements found")
