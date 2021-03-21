# for i in range(2):
#     for j in range(3):
#         print ("{}:{}".format (i,j), end=" ")
#     print ( )

# nama = []
# matkul = []
# z = 0

# n  = int(input ("Jumlah mahasiswa = "))
# m = int(input("Jumlah Matkul: "))
# for x in range (n):
#     name = input("Nama  = ")
#     nama.append(name)
#     for y in range (m):
#         matakuliah = input("Matakuliah: ")
#         matkul.append(matakuliah)

# for x in range (n):
#     print(x+1,".",nama[x] )
#     for y in range (m):
#         print ("---> ", matkul[z])
#         z += 1

# matkul = [[1,2,3],[4,5,6]]
# print(matkul[0][1])

# for x in range (1, 11):
#     for y in range (1, x+1):
#         print (y, end=",")
#     print()
# x = 11
# for u in range (1, 11):
#     for z in range (1, x-1):
#         print (z, end=",")
#     x -= 1
#     print()

for x in range (10, 0, -1):
    for y in range (1, x+1):
        print(y, end=",")
    print()