%Enrich the KB with ‘brother’, ‘sister’, ‘uncle’ and ‘aunt’ rules

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
male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').
male('Ratul').
male('Rafiq').
male('Rahim').
female('Rebeka').
female('Nusrat').
female('Tumpa').
female('Runa').

brother(X,Y):-
    parent(Z,X), parent(Z,Y), male(X), not(X=Y).
sister(X,Y):-
    parent(Z,X), parent(Z,Y), female(X), not(X=Y).
uncle(X,Y):-
    parent(Z,Y), brother(X,Z).
aunt(X,Y):-
    parent(Z,Y), sister(X,Z).

findBr:-
    write('Person Name: '),read(Pn),write('Brother name: '),
    brother(Br,Pn),write(Br),tab(5),fail.
findBr.

findSr:-
    write('Person Name: '),read(Pn),write('Sister name: '),
    sister(Sr,Pn),write(Sr),tab(5),fail.
findSr.

findUc:-
    write('Person Name: '),read(Pn),write('Uncle name: '),
    uncle(Uc,Pn),write(Uc),tab(5),fail.
findUc.

findAn:-
    write('Person Name: '),read(Pn),write('Aunt name: '),
    aunt(An,Pn),write(An),tab(5),fail.
findAn.









