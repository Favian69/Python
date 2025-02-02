# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

#++++++++3-----------10+++++++++

InputUser = float(input("Masukan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10 \n:"))

#++++++++3----------
# Memeriksa angka kurang dari 3
IsKurangDari = (InputUser < 3)
print("Kurang dari 3 =", IsKurangDari)

#-------10++++++++++
# Memeriksa angka lebih dari 10
IsLebihDari = (InputUser > 10)
print("Lebih dari 10 = ", IsLebihDari)

#++++++++3-----------10+++++++++
isCorrect = IsKurangDari or IsLebihDari
print('Hasil dari angka yang anda masukan :', isCorrect)

print("\n",10*'=','\n')

#--------3++++++++++++10---------
# kasus irisan

InputUser = float(input("Masukan angka yang bernilai \nlebih dari 3 \natau \nkurang dari 10 \n:"))

#--------3+++++++++++
IsLebihDari = (InputUser > 3)
print("Lebih dari 3 =", IsLebihDari)

#++++++++10-----------
IsKurangDari = (InputUser < 10)
print("Kurang dari 10 =", IsKurangDari)

#--------3++++++++++++10---------
isCorrect = IsLebihDari and IsKurangDari
print("Hasil dari angka yang anda masukan :", isCorrect)