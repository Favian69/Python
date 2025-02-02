#Operasi dan Menipulasi String Penting!!!!

# 1. Menyambungkan antar String (Concatenate)
nama_pertama = "Ilham"
nama_tengah = "D"
nama_akhir = "Mey"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang String
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + ' = ' + str(panjang))

# 3. operator untuk String

# mengecek apakah ada komponen char dalam string

I = "I"
status = I in nama_lengkap
print("I dalam " + nama_lengkap + " = " + str(status))

d = 'd'
status = d in nama_lengkap
print("d dalam " + nama_lengkap + " = " + str(status))

d = 'd'
status = d not in nama_lengkap
print("d tidak dalam " + nama_lengkap + " = " + str(status))

D = "D"
status = D not in nama_lengkap
print("D tidak dalam " + nama_lengkap + " = " + str(status))

# mengulang string
print("Mewi "*10)
print(15*"Mewi ")

# indexing 
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-6 : " + nama_lengkap [6])
print("Index ke-(-1) : " + nama_lengkap [-1])
print("Index ke-(-2) : " + nama_lengkap [-2])
print("Index ke-(0:3) : " + nama_lengkap [0:3]) # tanda ":" adalah sampai, misal 1 sampai 10 (1:10)
print("Index ke-(4:9) : " + nama_lengkap [4:9])
print("Index ke-(0,2,4,6,8,10) : " + nama_lengkap [0:10:2]) # 2 menandakan dia melangkah, misal 2,4,6,8

# item paling kecil
print("Paling kecil : " + min(nama_lengkap))

# item paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord("y")
print("ASCII code untuk y adalah : " + str(ascii_code))

data = 121
print("char untuk ASCII 114 adalah " + chr(data))

# 4. operator dalam bentuk method 

data = "Ripa surepa pararepa"
jumlah = data.count("a") # method count dalam string untuk menghitung char yang dipilih
print("Jumlah a dalam " + data + " = " + str(jumlah))

data = "Ilham Rizkiawan"
jumlah = data.count("i")
print("Jumlah i dalam " + data + " = " + str(jumlah))