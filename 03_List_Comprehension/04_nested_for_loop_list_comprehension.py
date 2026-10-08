#printing matrix using list comprehension
M=[[1,2,3],[4,5,6],[7,8,9]]
r=[M[r][c] for r in range(len(M)) for c in range(len(M[r]))]
print(r)

#getting indexes of matrix
result=[(r,c) for r in range(len(M)) for c in range(len(M[r]))]
print(result)
