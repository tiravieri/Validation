import csv
import numpy as np
import pandas as pd

data = pd.read_csv("DataTrain_Tugas3_AI.csv")
#dataB = pd.read_csv("DataTrain_Tugas3_AI.csv", skiprows=21, nrows= 20)
data.set_index("Index", inplace=True)  #mensetting data index dari dataframe ke atribut "Index"
#next(dataB)
# SET NUMBER N = 4
final = []              #LIST -> HASIL PERHITUNGAN MENGGUNAKAN
K3hitung = []           #List untuk memasukkan 3 data hasil perhitungan terkecil -> K = 3
K4hitung = []           #List untuk memasukkan 4 data hasil perhitungan terkecil -> K = 4
K5hitung = []           #List untuk memasukkan 5 data hasil perhitungan terkecil -> K = 5
kelasK3 = []            #list JUMLAH PER kelas dalam 3 data = Y
kelasK4 = []            #list JUMLAH PER kelas dalam 4 data = Y
kelasK5 = []            #list JUMLAH PER kelas dalam 5 data = Y

persentasiK1 = 0           #variabel untuk menghitung persentasi dari tiap K
persentasiK3 = 0
persentasiK4 = 0
persentasiK5 = 0
q = 0

# K-FOLD CROSS VALIDATION
# K-FOLD CROSS, MEMBAGI KE 4 DATA
# DATA A = 1-200, DATA B = 201 - 400, DATA C = 401 - 600, DATA D = 601 - 800

# untuk mendapatkan rentang / range nya :
trainACD = range(201, 401)     # data A, C, D sebagai Data Train, Data B = Data Test
trainABD = range(401, 601)     # data A, B, D = Data Train, Data C = Data Test

# data.loc[<row selection>, <column selection>]

print("Data A sebagai data test : ")
for i in range(1, 201):
    for j in range(201, 801):
        pengurangan = abs(data.loc[i] - data.loc[j])
        hasil = pengurangan.iloc[0] + pengurangan.iloc[1] + pengurangan.iloc[2] + pengurangan.iloc[3] + pengurangan.iloc[4]
        y = data.iloc[j-1, 5]
        final.append([j, hasil, y])

    final = sorted(final, key=lambda x: x[1])
    # print("data ke-", i, "adalah ", final[0:5])  untuk mengecek hasil

    for m in range(0, 3):
        K3hitung.append(final[m][2])
    for o in range(0, 4):
        K4hitung.append(final[o][2])            #memasukkan data kedalam list berdasarakan jumlah K
    for p in range(0, 5):
        K5hitung.append(final[p][2])

    for h in range(0, 4):
        itungK3 = K3hitung.count(h)                 #menghitung kelas (0,1,2,3) dan dimasukan kedalam list
        kelasK3.append([h, itungK3])                #memasukkan hitungan ke dalam list kelasK3
        itungK4 = K4hitung.count(h)
        kelasK4.append([h, itungK4])
        itungK5 = K5hitung.count(h)
        kelasK5.append([h, itungK5])

    kelasK3 = sorted(kelasK3, key=lambda x: x[1], reverse=True)         #sorting isi kelas dengan jumlah (0,1,2,3) terbanyak dalam K =3
    kelasK4 = sorted(kelasK4, key=lambda x: x[1], reverse=True)
    kelasK5 = sorted(kelasK5, key=lambda x: x[1], reverse=True)
    K3 = kelasK3[0][0]
    K4 = kelasK4[0][0]          #memasukkan kelas dengan jumlah tertinggi
    K5 = kelasK5[0][0]
    K1 = final[0][2]
    # print("K1 = ", K1)
    # print("Count untuk K = 3 : ", kelasK3)          #hanya untuk mengecek kelas terbanyak
    # print("K3 = ", K3)                              #outputkan kelas dari data test dalam K tertentu
    # print("Count untuk K = 3 : ", kelasK4)
    # print("K4 = ", K4)
    # print("Count untuk K = 3 : ", kelasK5)
    # print("K5 = ", K5)
    if K1 == data.iloc[i-1, 5]:
        persentasiK1 += 1
    if K3 == data.iloc[i-1, 5]:
        persentasiK3 += 1
    if K4 == data.iloc[i-1, 5]:
        persentasiK4 += 1
    if K5 == data.iloc[i-1, 5]:
        persentasiK5 += 1

    final = []                                      #Mengosongkan isi list final, hitung, dan kelas
    K3hitung = []
    K4hitung = []
    K5hitung = []
    kelasK3 = []
    kelasK4 = []
    kelasK5 = []
    q += 1
akurasiK1 = (persentasiK1/q) * 100
akurasiK3 = (persentasiK3/q) * 100
akurasiK4 = (persentasiK4/q) * 100
akurasiK5 = (persentasiK5/q) * 100
print(q)
print("Akurasi K = 1 Adalah", "{:.2f}".format(akurasiK1), '%')
print("Akurasi K = 3 Adalah", "{:.2f}".format(akurasiK3), '%')
print("Akurasi K = 4 Adalah", "{:.2f}".format(akurasiK4), '%')
print("Akurasi K = 5 Adalah", "{:.2f}".format(akurasiK5), '%')
print("========================================")
print(" ")

print("Data B sebagai Data Test :")
for i in range(201, 401):
    for j in (x for x in range(1, 801) if x not in trainACD):
        pengurangan = abs(data.loc[i] - data.loc[j])
        hasil = pengurangan.iloc[0] + pengurangan.iloc[1] + pengurangan.iloc[2] + pengurangan.iloc[3] + \
                pengurangan.iloc[4]
        y = data.iloc[j - 1, 5]
        final.append([j, hasil, y])

    final = sorted(final, key=lambda x: x[1])

    for m in range(0, 3):
        K3hitung.append(final[m][2])
    for o in range(0, 4):
        K4hitung.append(final[o][2])  # memasukkan data kedalam list berdasarakan jumlah K
    for p in range(0, 5):
        K5hitung.append(final[p][2])

    for h in range(0, 4):
        itungK3 = K3hitung.count(h)  # menghitung kelas (0,1,2,3) dan dimasukan kedalam list
        kelasK3.append([h, itungK3])  # memasukkan hitungan ke dalam list kelasK3
        itungK4 = K4hitung.count(h)
        kelasK4.append([h, itungK4])
        itungK5 = K5hitung.count(h)
        kelasK5.append([h, itungK5])

    kelasK3 = sorted(kelasK3, key=lambda x: x[1],
                     reverse=True)  # sorting isi kelas dengan jumlah (0,1,2,3) terbanyak dalam K =3
    kelasK4 = sorted(kelasK4, key=lambda x: x[1], reverse=True)
    kelasK5 = sorted(kelasK5, key=lambda x: x[1], reverse=True)
    K3 = kelasK3[0][0]
    K4 = kelasK4[0][0]  # memasukkan kelas dengan jumlah tertinggi
    K5 = kelasK5[0][0]
    K1 = final[0][2]

    if K1 == data.iloc[i - 1, 5]:
        persentasiK1 += 1
    if K3 == data.iloc[i - 1, 5]:
        persentasiK3 += 1
    if K4 == data.iloc[i - 1, 5]:
        persentasiK4 += 1
    if K5 == data.iloc[i - 1, 5]:
        persentasiK5 += 1

    final = []  # Mengosongkan isi list final, hitung, dan kelas
    K3hitung = []
    K4hitung = []
    K5hitung = []
    kelasK3 = []
    kelasK4 = []
    kelasK5 = []
    q += 1
akurasiK1 = (persentasiK1 / q) * 100
akurasiK3 = (persentasiK3 / q) * 100
akurasiK4 = (persentasiK4 / q) * 100
akurasiK5 = (persentasiK5 / q) * 100
print(q)
print("Akurasi K = 1 Adalah", "{:.2f}".format(akurasiK1), '%')
print("Akurasi K = 3 Adalah", "{:.2f}".format(akurasiK3), '%')
print("Akurasi K = 4 Adalah", "{:.2f}".format(akurasiK4), '%')
print("Akurasi K = 5 Adalah", "{:.2f}".format(akurasiK5), '%')
print("========================================")
print(" ")

print("Data C sebagai Data Test :")
for i in range(401, 601):
    for j in (x for x in range(1, 801) if x not in trainABD):
        pengurangan = abs(data.loc[i] - data.loc[j])
        hasil = pengurangan.iloc[0] + pengurangan.iloc[1] + pengurangan.iloc[2] + pengurangan.iloc[3] + \
                pengurangan.iloc[4]
        y = data.iloc[j - 1, 5]
        final.append([j, hasil, y])

    final = sorted(final, key=lambda x: x[1])

    for m in range(0, 3):
        K3hitung.append(final[m][2])
    for o in range(0, 4):
        K4hitung.append(final[o][2])  # memasukkan data kedalam list berdasarakan jumlah K
    for p in range(0, 5):
        K5hitung.append(final[p][2])

    for h in range(0, 4):
        itungK3 = K3hitung.count(h)  # menghitung kelas (0,1,2,3) dan dimasukan kedalam list
        kelasK3.append([h, itungK3])  # memasukkan hitungan ke dalam list kelasK3
        itungK4 = K4hitung.count(h)
        kelasK4.append([h, itungK4])
        itungK5 = K5hitung.count(h)
        kelasK5.append([h, itungK5])

    kelasK3 = sorted(kelasK3, key=lambda x: x[1],
                     reverse=True)  # sorting isi kelas dengan jumlah (0,1,2,3) terbanyak dalam K =3
    kelasK4 = sorted(kelasK4, key=lambda x: x[1], reverse=True)
    kelasK5 = sorted(kelasK5, key=lambda x: x[1], reverse=True)
    K3 = kelasK3[0][0]
    K4 = kelasK4[0][0]  # memasukkan kelas dengan jumlah tertinggi
    K5 = kelasK5[0][0]
    K1 = final[0][2]

    if K1 == data.iloc[i - 1, 5]:
        persentasiK1 += 1
    if K3 == data.iloc[i - 1, 5]:
        persentasiK3 += 1
    if K4 == data.iloc[i - 1, 5]:
        persentasiK4 += 1
    if K5 == data.iloc[i - 1, 5]:
        persentasiK5 += 1

    final = []  # Mengosongkan isi list final, hitung, dan kelas
    K3hitung = []
    K4hitung = []
    K5hitung = []
    kelasK3 = []
    kelasK4 = []
    kelasK5 = []
    q += 1
akurasiK1 = (persentasiK1 / q) * 100
akurasiK3 = (persentasiK3 / q) * 100
akurasiK4 = (persentasiK4 / q) * 100
akurasiK5 = (persentasiK5 / q) * 100
print(q)
print("Akurasi K = 1 Adalah", "{:.2f}".format(akurasiK1), '%')
print("Akurasi K = 3 Adalah", "{:.2f}".format(akurasiK3), '%')
print("Akurasi K = 4 Adalah", "{:.2f}".format(akurasiK4), '%')
print("Akurasi K = 5 Adalah", "{:.2f}".format(akurasiK5), '%')
print("========================================")
print(" ")

print("Data D sebagai Data Test :")
for i in range(601, 801):
    for j in range(1, 601):
        pengurangan = abs(data.loc[i] - data.loc[j])
        hasil = pengurangan.iloc[0] + pengurangan.iloc[1] + pengurangan.iloc[2] + pengurangan.iloc[3] + \
                pengurangan.iloc[4]
        y = data.iloc[j - 1, 5]
        final.append([j, hasil, y])

    final = sorted(final, key=lambda x: x[1])

    for m in range(0, 3):
        K3hitung.append(final[m][2])
    for o in range(0, 4):
        K4hitung.append(final[o][2])  # memasukkan data kedalam list berdasarakan jumlah K
    for p in range(0, 5):
        K5hitung.append(final[p][2])

    for h in range(0, 4):
        itungK3 = K3hitung.count(h)  # menghitung kelas (0,1,2,3) dan dimasukan kedalam list
        kelasK3.append([h, itungK3])  # memasukkan hitungan ke dalam list kelasK3
        itungK4 = K4hitung.count(h)
        kelasK4.append([h, itungK4])
        itungK5 = K5hitung.count(h)
        kelasK5.append([h, itungK5])

    kelasK3 = sorted(kelasK3, key=lambda x: x[1],
                     reverse=True)  # sorting isi kelas dengan jumlah (0,1,2,3) terbanyak dalam K =3
    kelasK4 = sorted(kelasK4, key=lambda x: x[1], reverse=True)
    kelasK5 = sorted(kelasK5, key=lambda x: x[1], reverse=True)
    K3 = kelasK3[0][0]
    K4 = kelasK4[0][0]  # memasukkan kelas dengan jumlah tertinggi
    K5 = kelasK5[0][0]
    K1 = final[0][2]
    # Mengecek apakah Y = dengan klasifikasi pada K, jika sama nilainya bertambah 1
    if K1 == data.iloc[i - 1, 5]:
        persentasiK1 += 1
    if K3 == data.iloc[i - 1, 5]:
        persentasiK3 += 1
    if K4 == data.iloc[i - 1, 5]:
        persentasiK4 += 1
    if K5 == data.iloc[i - 1, 5]:
        persentasiK5 += 1

    final = []  # Mengosongkan isi list final, hitung, kelas, dll
    K3hitung = []
    K4hitung = []
    K5hitung = []
    kelasK3 = []
    kelasK4 = []
    kelasK5 = []
    q += 1
#Menghitung Akurasi untuk tiap nilai K
akurasiK1 = (persentasiK1 / q) * 100
akurasiK3 = (persentasiK3 / q) * 100
akurasiK4 = (persentasiK4 / q) * 100
akurasiK5 = (persentasiK5 / q) * 100
print("Akurasi dari ", q, " data")
print("Akurasi K = 1 Adalah", "{:.2f}".format(akurasiK1), '%')
print("Akurasi K = 3 Adalah", "{:.2f}".format(akurasiK3), '%')
print("Akurasi K = 4 Adalah", "{:.2f}".format(akurasiK4), '%')
print("Akurasi K = 5 Adalah", "{:.2f}".format(akurasiK5), '%')
print("========================================")
print(" ")