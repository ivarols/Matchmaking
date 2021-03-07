# Matchmaking
This program takes in two matrices containing score and can thereafter calculate the best matches.


This matchmaking program takes in two matrices of potentially differing dimansions. Given that one must have the same dimension as the transpose matrix of the other.
(dim(M1)=dim(M2^T)) or (dim(M1^T)=dim(M2))

This program can handle equal totalscoreing and will chose the one where the scoredicrepacy is the smallest.
Tough the chooseíng is not completely optimzed. Matches of earlier people in the matrices get better matches if it comes to an equality with a later persons match.

It will also make sure it finds the best match for each and every person with in the matrix with smallest number of people or match one-to-one of the matrices have the same size.
