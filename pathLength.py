#Define a recursive procedure to find the length of a path between two vertices of a directed weighted graph

def rec_pathLength(start,end,length):
    if(start,end) in graph.keys():
        global pathFound
        pathFound=True
        print(length+graph[(start,end)],end=' ')
        
    for (i,j) in graph.keys():
        if i==start:
            rec_pathLength(j,end,length+graph[(i,j)])

graph={('i','a'):35,('i','b'):45,('a','c'):20,('a','d'):30,('b','d'):25,('b','e'):35,
       ('b','f'):27,('c','d'):30,('c','g'):47,('d','g'):30,('e','g'):25}

pathFound=False

start = str(input('Enter starting vertices: '))
end = str(input('Enter ending vertices: '))

print('The lengths of the path are: ',end=' ')
rec_pathLength(start,end,0)

if(not pathFound):
    print(0)



