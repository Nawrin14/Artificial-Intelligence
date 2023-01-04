#Write Python code to find the grandparent(s) of somebody

parentList=[('parent', 'Hasib', 'Rakib'),
            ('parent', 'Rakib', 'Sohel'),
            ('parent', 'Rakib', 'Rebeka'),
            ('parent', 'Rashid', 'Hasib'),
            ('parent', 'Hasib', 'Runa'),
            ('parent', 'Nusrat', 'Sohel'),
            ('parent', 'Ratul', 'Tumpa'),
            ('parent', 'Rafiq', 'Ratul'),
            ('parent', 'Rafiq', 'Nusrat'),
            ('parent', 'Hasib', 'Rahim')]

X=str(input("Grandchildren: "))

print('Grandparent:', end=' ')

i=0
gcFound=False
gpFound=False

while(i<len(parentList)):
    if ((parentList[i][0] == 'parent') & (parentList[i][2] == X)):
        gcFound=True
        for j in range((len(parentList))):
            if ((parentList[j][0] == 'parent') & (parentList[i][1] == parentList[j][2])):
                print(parentList[j][1], end=' ')
                gpFound=True
    i+=1

if((not gcFound) & (not gpFound)):
    print("Grandchildren not found in the list.")
elif(not gpFound):
    print("Grandparent not found in the list.")
    

