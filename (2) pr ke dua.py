# (2) pr ke dua

#+++++++++++0----------5+++++++++++8----------11+++++++++++

InputUser = float(input("Masukan angka yang bernilai \nkurang dari 0 \nlebih dari 5 \nkurang dari 8 \nlebih dari 11 \n:"))

#+++++++++++0----------
IsKurangDari = (InputUser < 0)
print('Kurang dari 0 =', IsKurangDari)

#----------5+++++++++++
IsLebihDari = (InputUser > 5)
print('Lebih dari 5 =', IsLebihDari)

#+++++++++++8----------
IsKurangDari = (InputUser < 8)
print('Kurang dari 8 =', IsKurangDari)

#----------11+++++++++++
IsLebihDari = (InputUser > 11)
print('Lebih dari 11 =', IsLebihDari)

#+++++++++++0----------5+++++++++++8----------11+++++++++++
isCorrect = IsKurangDari and IsLebihDari, IsKurangDari and IsLebihDari
print("Hasil dari angka yang anda masukan :", isCorrect)