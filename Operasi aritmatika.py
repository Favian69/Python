# Operasi aritmatika 

a = 10
b = 3

# 1. operasi tambah +
hasil = a + b
print(a,'+',b, '=',hasil)

# 2. operasi pengurangan -
hasil = a - b
print(a,'-',b, '=',hasil)

# 3. operasi perkalian *
hasil = a * b
print(a,'*',b, '=',hasil)

# 4. operasi pembagian /
hasil = a / b
print(a,'/',b, '=',hasil)

# 5. operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b, '=',hasil)

# 6. operasi modulus %
hasil = a % b
print(a,'%',b, '=',hasil)

# 7. operasi floor devision //
hasil = a // b
print(a,'//',b, '=',hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. eksponen **
    3. perkalian dan kawan kawan * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+','x','/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# kurung akan mengambil langkah paling pertama

hasil = (x + y) * z
print(x,'+',y,'*',z,'=',hasil)

