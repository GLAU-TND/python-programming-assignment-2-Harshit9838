#Problem 2

h=eval(input())
h=[str(i) for i in h]
h.sort()
a=''
for i in range(len(h)-1):
    if h[i][0]==h[i+1][0] and len(h[i])<len(h[i+1]):
        b=h[i]
        h[i]=h[i+1]
        h[i+1]=b
for i in range(len(h)-1,-1,-1):
    a=a+h[i]
print(int(a))
