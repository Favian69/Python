# Latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celsius = float(input('Masukan suhu dalam celsius : '))
print("Suhu adalah : ",celsius,"Celsius")

#Reamur 
reamur = (4/5) * celsius #ini rumus suhunya
print("Suhu dalam reamur adalah : ",reamur,"Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celsius) + 32 #ini rumus suhunya
print("Suhu dalam fahrenheit adalah : ",fahrenheit,"Fahrenheit")

#Kelvin
kelvin = celsius + 273 #ini rumus suhunya
print("Suhu dalam kelvin adalah : ",kelvin,"Kelvin")

