#Write a program to calculate the heuristic for 8 queen problem where the heuristic is the number of attacking pairs

def sameRow(l):
    global h
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]:
                h+=1
                
def digonallyUp(l):
    global h
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]+j-i:
                h+=1
                
def digonallyDown(l):
    global h
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]-(j-i):
                h+=1
                
h=0
l=[2,6,1,7,4,0,3,5]
sameRow(l)
digonallyUp(l)
digonallyDown(l)

print('Heuristic: ',h)
