import pandas as pd

dataTrain = pd.read_csv("DataTrain_Tugas3_AI.csv")
dataTest = pd.read_csv("DataTest_Tugas3_AI.csv")
dataTrain.set_index("Index", inplace=True)
dataTest.set_index("Index", inplace=True)

# Variabel :
final = []
K5hitung = []
kelasK5 = []
klasifikasi = []
for i in range(0, 200):
    for j in range(0, 800):
        # print(dataTest.iloc[i, 0:5])
        pengurangan = abs(dataTest.iloc[i, 0:5] - dataTrain.iloc[j, 0:5])
        hasil = pengurangan.iloc[0] + pengurangan.iloc[1] + pengurangan.iloc[2] + pengurangan.iloc[3] + \
                pengurangan.iloc[4]
        y = dataTrain.iloc[j, 5]
        final.append([j+1, hasil, y])
    final = sorted(final, key=lambda x: x[1])
    #print(final[0:5])

    for p in range(0, 5):
        K5hitung.append(final[p][2])

    for h in range(0, 4):
        itungK5 = K5hitung.count(h)
        kelasK5.append([h, itungK5])

    kelasK5 = sorted(kelasK5, key=lambda x: x[1], reverse=True)
    #print(kelasK5)
    klasifikasi.append(kelasK5[0][0])
    final = []
    K5hitung = []
    kelasK5 = []
#print(klasifikasi)

for i in range(0, 200):
    if i is 0:
        baca = open("TebakanTugas3.csv", 'w')                #membuka file dan menimpanya(w = menulis dan menghapus file lama)
        baca.write(str(klasifikasi[i]))                        #menulis data pada file csv
        baca.write("\n")
        baca.close()
    elif i is not 0:
        baca = open("TebakanTugas3.csv", 'a')                #mode 'a' = menambah data di akhir baris
        baca.write(str(klasifikasi[i]))                        #menulis data pada file csv
        baca.write("\n")
        baca.close()                                        #menutup file agar file tersave
