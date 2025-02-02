 # Tugas (PR) Konversi suhu fahrenheit ke kelvin, kelvin ke fahrenheit

# Fahrenheit ke satuan kelvin 
fahrenheit = float(input('Masukan suhu dalam Fahrenheit : '))
print("Suhu adalah : ",fahrenheit,"Fahrenheit")

# Kelvin 
kelvin = 5/9 * (fahrenheit - 32) + 273
print("Suhu dalam kelvin : ",kelvin,"Kelvin")


# Kelvin ke satuan fahrenheit
kelvin = float(input('Masukan suhu dalam kelvin : '))
print("Suhu adalah : ",kelvin,"Kelvin")

# fahrenheit 
fahrenheit = 9/5 * (kelvin - 273) + 32
print("Suhu dalam fahrenheit : ",fahrenheit,"Fahrenheit")