#this function creates the matrix that gives the length of the LCS
#the matrix can be used to find the path that gives the LCS
def LCS_matrix(w1, w2):

    l1 = len(w1)
    l2 = len(w2)

    #define an auxillary array used to compute the LCS
    D1 = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            #if the letters are equal
            if w1[i-1] == w2[j-1]:
                D1[i][j] = D1[i-1][j-1] + 1
            #if the number in the row above is larger
            #than the number in the current column
            elif D1[i-1][j] >= D1[i][j-1]:
                D1[i][j] = D1[i-1][j]
            #if the number in the column to the left is larger
            #than the number in the current row. 
            else:
                D1[i][j] = D1[i][j-1]
                
    return D1

#this function tracks backward to find the LCS
#it follows the path laid out in the matrix created by LCS_matrix
def find_lcs(a, b, D1):

    D2 = []

    while a > 0 and b > 0:
        #if the number in the row above is equal to
        #the current index
        if D1[a-1][b] == D1[a][b]:
            a = a - 1
        #if the number in the column to the left is equal to
        #the current index
        elif D1[a][b-1] == D1[a][b]:
            b = b - 1    
        #otherwise add one to the upper left diagonal
        else:
            D2.insert(0, w1[a - 1])
            a = a - 1
            b = b - 1

    return D2

#main
w1 = input("Enter a Word: ")
w2 = input("Enter another Word: ")

lcsM = LCS_matrix(w1, w2)
lcs = find_lcs(len(w1), len(w2), lcsM)

print(lcs)

