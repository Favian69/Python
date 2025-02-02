# (1) pr ke satu

#----------0+++++++++++5----------8+++++++++++11----------

InputUser = float(input("Masukan angka yang bernilai \nlebih dari 0 \nkurang dari 5 \nlebih dari 8 \nkurang dari 11 \n:"))

#----------0+++++++++++
IsLebihDari = (InputUser > 0)
print('Lebih dari 0 =', IsLebihDari)

#+++++++++++5----------
IsKurangDari = (InputUser < 5)
print('Kurang dari 5 =', IsKurangDari)

#----------8+++++++++++
IsLebihDari = (InputUser > 8)
print('Lebih dari 8 =', IsLebihDari)

#+++++++++++11----------
IsKurangDari = (InputUser < 11)
print('Kurang dari 11 =', IsKurangDari)

#----------0+++++++++++5----------8+++++++++++11----------
isCorrect = IsLebihDari or IsKurangDari, IsLebihDari or IsKurangDari
print("Hasil dari angka yang anda masukan :", isCorrect)