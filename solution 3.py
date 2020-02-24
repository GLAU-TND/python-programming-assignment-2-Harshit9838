#Problem 3

b=bin(int(input()))
a=1
c=0
for i in range(len(b)-3):
    if b[i+2]==b[i+3]:
        a+=1
    else:
        c=max(c,a)
        a=1
        continue
print(c)
