# Operator Assignment
# adalah operasi yang dapat dilakukan dengan penyingkatan

a = 5 # ini adalah assignment
print("Nilai a =",a)

print("\nPertambahan")
a += 1 # penyingkatan dari a = a + 1
print("Nilai a += 1, nilai a menjadi",a)

print("\nPengurangan")
a -= 2 # penyingkatan dari a = a - 1
print("Nilai a -= 1, nilai a menjadi",a)

print("\nPerkalian")
a *= 5 # penyingkatan dari a = a * 1
print("Nilai a *= 1, nilai a menjadi",a)

print("\nPembagian")
a /= 2 # penyingkatan dari a = a / 1
print("Nilai a /= 1, nilai a menjadi",a)

# Modulus dan floor division

b = 10
print("\nNilai b =",b)

print("\nModulus")
b %= 3
print("Nilai b %= 3, nilai b menjadi",b)

print("\nFloor division")
b //= 3
print("Nilai b //= 3, nilai b menjadi",b)

print("\nModulus")
b %= 3
print("Nilai b %= 3, nilai b menjadi",b)

a = 5
print("\nNilai a =",a)
print("\nPerpangkatan")
a **= 3
print("Nilai a **= 3, nilai a menjadi",a)

# Operasi bitwise
# OR
print("\nOR")
c = True
print("\nNiai c =",c)
c |= False
print("Nilai c |= False, nilai a menjadi",c)

c = True
print("\nNiai c =",c)
c |= True
print("Nilai c |= True, nilai a menjadi",c)

# AND
print("\nAND")
c = True
print("\nNiai c =",c)
c &= False
print("Nilai c &= False, nilai a menjadi",c)

c = True
print("\nNiai c =",c)
c &= True
print("Nilai c &= True, nilai a menjadi",c)

#XOR
print("\nXOR")
c = True
print("\nNiai c =",c)
c ^= False
print("Nilai c ^= False, nilai a menjadi",c)

c = True
print("\nNiai c =",c)
c ^= True
print("Nilai c ^= True, nilai a menjadi",c)

# geser geser
print("\nRight AND Left")
d = 0b0100
print("\nNilai d = ",format(d,'04b'))
d >>= 2
print("Nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("Nilai d <<= 1, nilai d menjadi",format(d,'04b'))