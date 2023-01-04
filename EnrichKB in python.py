#Enrich the KB with ‘brother’, ‘sister’, ‘uncle’ and ‘aunt’ rules

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

genderList=[('male','Hasib'),('male','Rakib'),('male','Sohel'),
            ('male','Rashid'),('male','Ratul'),('male','Rafiq'),
            ('male','Rahim'),('female','Rebeka'),('female','Runa'),
            ('female','Nusrat'),('female','Tumpa')]

X=str(input("Person Name: "))
Y=str(input("Relation: "))
print(Y,"name:",end='')

def Brother(X):
    i=0
    nameFound=False
    brotherFound=False

    while(i<len(parentList)):
        if ((parentList[i][0] == 'parent') & (parentList[i][2] == X)):
            nameFound=True
            for j in range((len(parentList))):
                if ((parentList[j][0] == 'parent') & (parentList[i][1] == parentList[j][1])
                    & (parentList[i][2] != parentList[j][2])):
                    for k in range((len(genderList))):
                        if ((genderList[k][0] == 'male') & (genderList[k][1] == parentList[j][2])):
                            print(parentList[j][2], end=' ')
                            brotherFound=True
        i=i+1

    if((not nameFound) or (not brotherFound)):
        return False
    else:
        return True

def Sister(X):
    i=0
    nameFound=False
    sisterFound=False

    while(i<len(parentList)):
        if ((parentList[i][0] == 'parent') & (parentList[i][2] == X)):
            nameFound=True
            for j in range((len(parentList))):
                if ((parentList[j][0] == 'parent') & (parentList[i][1] == parentList[j][1])
                    & (parentList[i][2] != parentList[j][2])):
                    for k in range((len(genderList))):
                        if ((genderList[k][0] == 'female') & (genderList[k][1] == parentList[j][2])):
                            print(parentList[j][2], end=' ')
                            sisterFound=True
        i=i+1

    if((not nameFound) or (not sisterFound)):
        return False
    else:
        return True

def Uncle(X):
    i=0
    nameFound=False
    uncleFound=False

    while(i<len(parentList)):
        if ((parentList[i][0] == 'parent') & (parentList[i][2] == X)):
            nameFound=True
            Z = parentList[i][1]
            if(Brother(Z)):
               uncleFound=True
        i=i+1

    if((not nameFound) or (not uncleFound)):
        return False
    else:
        return True

def Aunt(X):
    i=0
    nameFound=False
    auntFound=False

    while(i<len(parentList)):
        if ((parentList[i][0] == 'parent') & (parentList[i][2] == X)):
            nameFound=True
            Z = parentList[i][1]
            if(Sister(Z)):
               auntFound=True
        i=i+1

    if((not nameFound) or (not auntFound)):
        return False
    else:
        return True

if (Y == 'Brother'):
    findBrother = Brother(X)
    if (not findBrother):
        print("Not found")
elif (Y == 'Sister'):
    findSister = Sister(X)
    if (not findSister):
        print("Not found")
elif (Y == 'Uncle'):
    findUncle = Uncle(X)
    if (not findUncle):
        print("Not found")
elif (Y == 'Aunt'):
    findAunt = Aunt(X)
    if (not findAunt):
        print("Not found")
else:
    print('Relation not found')






