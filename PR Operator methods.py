# PR Operator methods

# isaplha() <-- untuk mengecek semuanya huruf
huruf = "A silent voice"
cek_huruf = huruf.isalpha()
print(huruf + " adalah = ",cek_huruf) # akan False jika ada simbol

huruf = "Asilentvoice"
cek_huruf = huruf.isalpha()
print(huruf + " adalah = ",cek_huruf) # akan True jika semuanya adalah huruf (tidak boleh ada simbol,spasi juga termasuk)

# isalnum() <-- huruf dan angka
huruf = "."
angka = "6serpent9"

cek_huruf = huruf.isalnum()
print(huruf + " adalah = ",cek_huruf) # akan False jika ada simbol

cek_angka = angka.isalnum()
print(angka + " adalah = ",cek_angka) # akan True jika semua karakter alfanumerik (angka dan huruf)

# isdecimal() <-- angka saja
desimal = "6.969600"
cek_desimal = desimal.isdecimal()
print(desimal + " = " + str(cek_desimal))

desimal = "6969600"
cek_desimal = desimal.isdecimal()
print(desimal + " = " + str(cek_desimal)) # True jika semua nomer

# contoh penerapan
#user_input = input("Enter a number: ") 
#if user_input.isdecimal(): 
    #print("Valid input") 
#else: 
    #print("Invalid input")

# isspace() <-- spasi, tab, newline
kata = "\t"
cek_kata = kata.isspace()
print(kata + " adalah = ",cek_kata)

kata = " "
cek_kata = kata.isspace()
print(kata + " adalah = ",cek_kata)

kata = "\n"
cek_kata = kata.isspace()
print(kata + " adalah = ",cek_kata)

kata = "Aowkowkwok False"
cek_kata = kata.isspace()
print(kata + " adalah = ",cek_kata)

