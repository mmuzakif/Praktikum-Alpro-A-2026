A = [[5, 3, 1],
[2, 8, 4],
[6, 0, 7]]


B = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

c_tambah = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
c_kurang =  [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
c_skalar = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for i in range(3):
    for j in range(3):
        g = A[i][j] + B[i][j]
        c_tambah[i][j] = g
 
for i in range(3):
    for j in range(3):
        g = A[i][j] - B[i][j]
        c_kurang[i][j] = g
 
for i in range(3):
    for j in range(3):
        g = 4 * A[i][j]
        c_skalar[i][j] = g
 
print("matriks tambah:")
print(c_tambah)
print("matriks kurang:")
print(c_kurang)
print("matriks skalar:")
print(c_skalar)