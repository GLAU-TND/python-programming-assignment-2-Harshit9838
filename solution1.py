#Problem 1

h=eval(input())
a=[min(h)]
b=min(h)[-1]
h.remove(min(h))
for i in h:
    for j in h:
        if b==j[0] and j[-1]!=a[0][0]:
            a.append(j)
            b=j[-1]
            h.remove(j)
            break
a=a+h
print(a)
