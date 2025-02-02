# Operator dalam bentuk methods

# 1. Merubah case dari string

# Merubah semua kata ke upper case
salam = "Wassup!"
print("Normal = ", salam)
salam = salam.upper()
print("Upper = ", salam)

# Merubah ke lower case
salam = "WASSUP!"
print("Normal = ", salam)
salam = salam.lower()
print("Lower = ", salam)

# 2. Pengecekan dengan isX methods

# Contoh pengecekan lower case
salam = "orewa saikyo da" #hasil akan True jika huruf kecil
pengecekan_lower = salam.islower() #hasil akan boolean True/False
print(salam + " is lower = " + str(pengecekan_lower))

# Contoh pengecekan upper case
salam = "ORE WA SAIKYO DA" #hasil akan True jika huruf besar
pengecekan_upper = salam.isupper() #hasil akan boolean True/False
print(salam + " is upper = " + str(pengecekan_upper))

# isaplha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline
# istitle() <-- semua kata yang diawali oleh huruf besar

judul = "A Silent Voice"
cek_judul = judul.istitle() #hasil boolean True/False
print(judul + " is title = " + str(cek_judul))

# 3. Mengecek komponen dengan starswith() dan endswith()
start = "Sung Jin Wo".startswith("Sung") #di awal
print("Start =", str(start))

end = "Sung Jin Wo".endswith("Wo") #di akhir
print("End =", str(end))

# 4. Penggabungan komponen join() dan split()
pisah = ["You're",'fucking','idiot']
gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "brain.washed.with.psychology"
print(gabungan)
print(gabungan.split('.'))

# 5. Alokasi karakter dengan rjust(), ljust(), dan center()
kanan = "kanan".rjust(10) 
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'") 

tengah = "tengah".center(20,"-") #bisa dikostumisasi kan ke bentuk -,./;'\
print("'"+tengah+"'") 

# kebalikannya --> strip()
tengah = tengah.strip("-") #menghapus elemen yang kita mau melalui split
print("'"+tengah+"'")