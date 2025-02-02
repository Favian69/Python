# Tipe tipe data : Integer (angka satuan tanpa koma), Float (angka dengan koma),
# String (kumpulan karakter), Biner (True/False), Data Complex, Dan Data c_double

#Data Integer (angka satuan tanpa koma)
data_integer = 11 
print("data : ", data_integer)
print("-bertipe : ", type(data_integer))

#Data Float (angka dengan koma)
data_float = 1.9
print("data : ", data_float)
print("-bertipe : ", type(data_float))

#Data String (Kumpulan karakter)
data_string = "ilham"
print("data : ", data_string)
print("-bertipe : ", type(data_string))


#Data Biner (True/False) (boolean)
data_bool = True
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))

#Data complex
data_complex = complex (6,9)
print("data : ", data_complex)
print("-bertipe : ", type(data_complex))

#Tipe bahasa dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double (10,5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))




