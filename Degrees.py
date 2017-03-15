import math
f=open('Colours.txt', 'r')
dict1={}
for line in f:
    line=line.rstrip()
    a=list(map(str,line.split()))
    dict1[a[1]] = a[0]

dict2={}
T=int(input())
for i in range(7):
    d,m,s,=(map(int,input().split()))
    colour=str(input())
    current = d + (m + s/60)/60
    current=math.sin(math.radians(current))-math.sin(math.radians(T))
    dict2[colour]=current
dict3={}
for key in dict1.keys():
    if key in dict2.keys():
        dict3[dict1.get(key)]=dict2.get(key)

A=list(dict3.keys())
B=list(dict3.values())
with open('Results.txt','a') as r:
    for i in range (len(A)):
        r.write(str(A[i])+ '  '+str(B[i])+'\n')
        i+=1

f.close()
