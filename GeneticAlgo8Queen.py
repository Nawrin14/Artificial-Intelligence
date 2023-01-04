#Implement Genetic Algorithm for 8 Queens problem. For the mutation step, use inversion mutation

import random

rand_comb=[]
score=[]
l1=[]
l2=[]
n=15

def fitnessScore(l):
    h=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]:
                h+=1

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]+j-i:
                h+=1

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]==l[i]-(j-i):
                h+=1

    return h

def crossover(l):
    global l1,l2    
    l1 = l[0][1][0:4] + l[1][1][4:8]
    l2 = l[1][1][0:4] + l[0][1][4:8]

def mutation():
    r = random.sample(range(0, 8), 2)
    a=sorted(r)[0]
    b=sorted(r)[1]
    
    l1[a:b] = l1[a:b][::-1]
    l2[a:b] = l2[a:b][::-1]
    
for i in range(n):
    res = random.sample(range(0, 8), 8)
    rand_comb.append(res)

for i in range(n):
    s = fitnessScore(rand_comb[i])
    score.append(s)

list_c = [[x, y] for x, y in zip(score, rand_comb)]
list_d = sorted(list_c)

while list_d[0][0]!=0:

    crossover(list_d)
    mutation()

    list_d.append([fitnessScore(l1),l1])
    list_d.append([fitnessScore(l2),l2])

    list_d = sorted(list_d)
    list_d = list_d[:-2]

print('Solution: ' + str(list_d[0][1]))

    
