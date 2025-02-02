# Operasi Komparasi

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("~~~~~LEBIH BESAR DARI >")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(a,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print("~~~~~KURANG DARI <")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("~~~~~LEBIH DARI SAMA DENGAN >=")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("~~~~~KURANG DARI SAMA DENGAN <=")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("~~~~~SAMA DENGAN ==")
hasil = a == 4
print(a,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan (!=)
print("~~~~~TIDAK SAMA DENGAN !=")
hasil = a != 2
print(a,'!=',3,'=',hasil)
hasil = b != 4
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 'is' sebagai komparasi objek identitas
x = 5 
y = 5 # jika mau FALSE maka x,y harus berbeda nomor
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is 5 =',hasil)

# 'is not' sebagai komparasi objek identitas
x = 5 
y = 5# jika mau TRUE maka x,y harus berbeda nomor
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is 5 =',hasil)



