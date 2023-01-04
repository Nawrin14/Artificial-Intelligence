%Write Prolog code to find the grandparent(s) of somebody

parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').
parent('Hasib','Runa').
parent('Nusrat','Sohel').
parent('Ratul','Tumpa').
parent('Rafiq','Ratul').
parent('Rafiq','Nusrat').
parent('Hasib','Rahim').

grandchildren(X,Z):-
    parent(Z,Y),parent(Y,X).

findGp:-
    write('Grandchildren: '),read(Gc),write('Grandparent: '),		                grandchildren(Gc,Gp),write(Gp),tab(5),fail.
findGp.
