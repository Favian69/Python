# Operasi bitwise (operasi binary)

a = 9
b = 5

# bitwise OR (|)
c = a | b 
print("\n=============OR==============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------(|)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))

# bitwise AND (&)
c = a & b
print("\n=============AND=============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------(&)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))

# bitwise XOR (^)
c = a ^ b
print("\n=============XOR=============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('nilai :',b,' , binary :',format(b,'08b'))
print('---------------(^)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))

# bitwise NOT (~)
c = ~a
print("\n=============NOT=============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('---------------(~)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))
d = 0b00001001
e = 0b11111111
print('---------------(^)-------------')
print('nilai :',d^e,' , binary :',format(d^e,'08b'))

# shifting

# shift right (>>)
c = a >> 2
print("\n=============>>===============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('---------------(>>)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))

# shift left (<<)
c = a << 2
print("\n=============<<===============")
print('nilai :',a,' , binary :',format(a,"08b"))
print('---------------(<<)-------------')
print('nilai :',c,' , binary :',format(c,"08b"))


