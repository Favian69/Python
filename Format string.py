# Format string

# contoh generic

# string
string = "string".center(20,"=")
print(string)
nama = "ilham"
format_str = f"Nama = {nama}\n"
print(format_str)

# boolean
boolean = "boolean".center(20,"=")
print(boolean)
boolean = False
format_boolean = f"Boolean = {boolean}\n"
print(format_boolean)

# angka
angka = "angka".center(20,"=")
print(angka)
angka = 2007.7
format_str = f"Angka = {angka}\n"
print(format_str)

# bilangan bulat
angka = "angka".center(20,"=")
print(angka)
angka = 17
format_str = f"Bilangan bulat = {angka:d}\n" #d melambangkan bilangan bulat
print(format_str)

# bilangan dengn ordo ribuan
angka = "angka".center(20,"=")
print(angka)
angka = 200000000
format_str = f"Ribuan = {angka:,}\n" # , digunakan untuk mengubah ke ribuan
print(format_str)

# bilangan desimal
angka = "angka".center(20,"=")
print(angka)
angka = 2007.7890
format_str = f"Desimal = {angka:.2f}\n" # .2f digunakan untuk menandai 2 angka sehabis koma
print(format_str)

# menampilkan leading zero
angka = "angka".center(20,"=")
print(angka)
angka = 2007.7890
format_str = f"Desimal = {angka:09.3f}\n" # 010.3f digunakan untuk menambahkah space atau jumlah sesuai nomer (10) dan 0 untuk memberi angka 0 sebanyak 2 (karena datanya ada 9)
print(format_str)

# menampilkan tanda + atau -
angka = "angka".center(20,"=")
print(angka)
minus = -17
plus = +69.9090909
format_minus = f"Minus = {minus:+d}"
format_plus = f"plus = {plus:+.2f}\n" # + digunakan untuk menampilkan + 

print(format_minus)
print(format_plus)

# memformat persen
persen = "persen".center(20,"=")
print(persen)
persentase = 0.80
format_persen = f"Persen = {persentase:.2%}\n"
print(format_persen)

# melakukan format aritmatika di dalam palceholder
angka = "Aritmatika".center(20,"=")
print(angka)
harga = 2000000
barang = 90
format_hasil = f"Hasil = Rp. {harga*barang:,}\n"
print(format_hasil)

# format angka lain (binary, octal, hex)

angka = "Binary Octal Hex".center(20,"=")
print(angka)
angka = 177
format_binary = f"Binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)