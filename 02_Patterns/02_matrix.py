r,c=map(int,input("Enter matrix size:").split())  # get rows and columns
a=list(map(int,input("Enter matrix numbers:").split()))[:r*c]  # get only r*c numbers
M=[a[i*c:(i+1)*c] for i in range(r)]  # create the matrix row by row

#M=[[1,2,3],[11,22,33],[111,222,333]]

for i in range(len(M)):  # go through each row
    for j in range(len(M[0])):  # go through each column
        print(M[i][j],end=" ")  # print each element
    print()  # move to the next row
    