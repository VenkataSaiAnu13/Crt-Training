n=int(input())
if n<=0:
    print("invalid input")
else:
    arr=list(map(int,input().split()))
    k=int(input())
    if k==n:
             print("invalid input")
    else:
        first=arr[:n-k]
        last=arr[n-k:]
        res=[last+first]
        print(*res)
