#Implement Greedy Best First Search algorithm

def Best_first_search(graph,h,start,end):
    closed_list=[]
    open_list=[]
    path=[]
    final_path=[]

    for (x,y) in h:
        if x==start:
            open_list.append((y,x))

    while(open_list):

        open_list.sort()
        l=open_list[0][1]

        if l==end:
            print('Path: ')
            for i in range (len(closed_list)):
                print(closed_list[i][1], end='->')
            print(l)
            break

        for a in graph:
            if a[0]==l:
                for b in a:
                    for (k,z) in h:
                        if k==b and (z,k) not in open_list and (z,k) not in closed_list:
                            path.append((l,k))
                            open_list.append((z,k))

        
        closed_list.append(open_list[0])
        open_list.pop(0)
        
        if not open_list:
            print('No solution')

    
graph=[('s','a','b','c'),('a','b','d'),('b','d','h'),
            ('c','l'),('d','f'),('h','f','g'),('g','e'),
            ('l','i','j'),('i','k'),('j','k'),('k','e')]

h=[('s',10),('a',9),('b',7),('c',8),('d',8),('h',6),('l',6),
   ('f',6),('g',3),('i',4),('j',4),('k',3),('e',0)]


start=input('Enter starting node: ')
end=input('Enter ending node: ')

Best_first_search(graph,h,start,end)

