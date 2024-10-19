#Lakukan input test case
N = int(input())
#Deklarasi array "simpan" untuk menyimpan dan mengeluarkan output nanti
simpan = []

for _ in range(N):
    #Input integer M (jumlah elemen dalam array)
    M = int(input())
    #Deklarasi array "angka-angka" untuk menyimpan angka-angka yang bakalan dihitung modusnya
    angka_angka = list(map(int,input().split()))

    #Memastikan panjang array angka_angka dan jika len = 1 sudah pasti tidak ada modus dan print -1
    if len(angka_angka) == 1:
        print(-1)
    else:
        #Deklarasi dictionary "hitung" untuk menyimpan nilai count setiap elemen dari array "angka_angka"
        hitung = {}
        #For loop untuk menyimpan nilai count setiap angka, lalu di add ke set "hitung"
        for angka in angka_angka:
            hitung[angka] = angka_angka.count(angka)
        
        #Deklarasi variabel jumlah terbanyak untuk menyimpan jumlah tertinggi munculnya suatu angka
        jumlah_terbanyak = max(hitung.values()) 

        #Deklarasi array modus untuk menyimpang angka-angka yang menjadi modus (bisa ada lebih dari 1 modus)
        modus = []

        #For loop untuk mengecek angka-angka yang memiliki jumlah terbanyak, lalu akan dimasukan ke array modus
        for angka2, jumlah in hitung.items():
            if jumlah == jumlah_terbanyak:
                modus.append(angka2)
            
        #Melakukan proses untuk memasukan output ke array "simpan"
        if len(modus) == 1:
            simpan.append(f"{jumlah_terbanyak} * {modus[0]} = {jumlah_terbanyak * modus[0]}")
        else:
            #Deklarasi variabel angka string untuk menggabungan angka-angka modus menjadi bentuk perkalian dengan tanda '*'
            angka_string = '*'.join(map(str, modus))

            #Hitung perkalian semua angka modus
            hasil_kali = 1
            for angka_modus in modus:
                hasil_kali *= angka_modus

            #Append keduanya ke array simpan
            simpan.append(f"{angka_string} = {hasil_kali}") 



for output in simpan:
    print(output)