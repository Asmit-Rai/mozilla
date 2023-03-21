i=[4,3,2,5,2]
p=len(i)
y=0
for x in range(0,p):
    if i[x]==i[x-1] :
        y+=1
print(y)
