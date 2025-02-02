data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = '1. ini menggunakan single quote'
print(data)

data = "2. ini menggunakan double quote"
print(data)

print("'Mey rahmawati alias mey'")
print('"Mey rahmawati alias mey"')
print("ini hari juma't") # dikala ada kata yang menggunakan tanda ', maka di eksekusi oleh double quote "

# 2. menggunakan tanda \

# a. membuat tanda ' menjadi string
print('mari sholat juma\'t') # bisa juga menggunakan tanda \ biar ' masuk menjadi string
print('g\'day, isn\'t it?')

# b. menggunakan backslash
print('C:\\user\\ucup') # agar bisa di print harus menggunakan double backslash 

# c. tab (\t) : berfungsi untuk menjauhkan antar karakter
print('ripa\t\t\tmewi')

# d. backspace (menyambungkan antar karakter)
print("ilham \bmey")

# e. newline (enter atau garis baru)
print('baris pertama.\nbaris kedua') # LF : line feed -> UNix, Linux, macOS
print('baris pertama.\rbaris kedua ') # CR : carriage return -> Ucorn
print('baris pertama.\r\nbaris kedua') # CRFL : carriage return line feed -> Windows

# 3. String Literal atau RAW

# menggunakan raw string
print(r'C:\new folder') # fungsi raw adalah untuk menampilkan semua yang berada area, agar bisa diubah ke string

# tidak menggunakan raw string
print('C:\\new folder')

# multiline literal string dan RAW
print(r"""
Nama : ilam\mewi
Kelas : 11\11
Jurusan : TP\DKV
Catatan : mewi bububb aku woeeeeee   # apabila ditambah RAW semua elemen bakalan ke print string
""")

