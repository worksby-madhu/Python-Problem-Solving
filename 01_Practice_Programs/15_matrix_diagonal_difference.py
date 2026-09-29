n = 4

matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 200, 300],
    [400, 500, 600, 700]
]

D1 = 0
D2 = 0

for i in range(n):
    for j in range(n):
        if i == j:
            D1 += matrix[i][j]

        if i + j == n - 1:
            D2 += matrix[i][j]

difference = abs(D1 - D2)

print("Primary diagonal sum:", D1)
print("Secondary diagonal sum:", D2)
print("Diagonal difference:", difference)