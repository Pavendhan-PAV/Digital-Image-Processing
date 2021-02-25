import random

# input size
r = int(input("Enter number of rows of matrix: "))
c = int(input("Enter number of columns of matrix: "))
size = r * c
matrix = []

# matrix generation
for i in range(r):
    a = []
    for j in range(c):
        a.append(random.randint(0, 9))
    matrix.append(a)

# print generated matrix
print("\nGENERATED MATRIX--")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print("")


# sum
Sum = 0
for i in range(r):
    for j in range(c):
        Sum += matrix[i][j]
print("\nSUM: ", Sum)


# maximum
Max = matrix[0][0]
for i in range(r):
    for j in range(c):
        if Max < matrix[i][j]:
            Max = matrix[i][j]
print("MAXIMUM:", Max)


# mean
mean = Sum / size
print("MEAN: ", mean)


# median (matri -> 1D array)
temp = matrix
for i in range(1, len(temp)):
    temp[0].extend(temp[i])
flat_matrix = sorted(temp[0])
if size % 2 == 0:
    median = (
        flat_matrix[(len(flat_matrix)) // 2 - 1] + flat_matrix[(len(flat_matrix)) // 2]
    )
    median /= 2
else:
    median = flat_matrix[(len(flat_matrix)) // 2]
print("MEDIAN: ", median)


# mode
f_dist = {x: flat_matrix.count(x) for x in set(flat_matrix)}
print("MODE: ", max(f_dist, key=f_dist.get))


# standard deviation
variance = sum(pow(x - mean, 2) for x in flat_matrix) / len(flat_matrix)
std = pow(variance, 0.5)
print("STANDARD DEVIATION: ", std)


# frequency distribution
print("\nFREQUENCY DISTRIBUTION ---\nDATA\tFREQUENCY")
f_dist = {x: flat_matrix.count(x) for x in set(flat_matrix)}
for i in sorted(f_dist):
    print(i, "\t", f_dist[i])
