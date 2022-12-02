def hitungKata(strr, kata) :
    jlh = 0
    if kata in strr :
        jlh = jlh + 1
        strr.replace(kata, " ")
        if kata in strr:
            jlh = jlh + 1
            strr.replace(kata, " ")
            
    return jlh

def ubahKata(strr, kataDiubah, kataPengganti) :
    if kataDiubah in strr :
        return strr.replace(kataDiubah, kataPengganti)
        
print("======= Program Manipulasi String =======")
print("Pilihan Menu : ")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan = int(input("Pilihan anda : "))

if pilihan == 2 :
    strr = input("Masukkan sebuah kalimat/kata : ")
    kataDiubah = input("Masukkan kata yang ingin diubah : ")
    kataPengganti = input("Masukan kata pengganti : ")
    res = ubahKata(strr, kataDiubah, kataPengganti)
    print ("String berhasil diubah menjadi : "  + res)
    
elif pilihan == 1:
    strr = input("Masukkan sebuah kalimat/kata : ")
    kataHitung = input("Masukkan kata yang ingin dihitung : ")
    res = hitungKata(strr, kataHitung)
    print("Terdapat sebanyak " + str(res) + " kata " + kataHitung + " di dalam kalimat")
    
elif pilihan == 3 :
    strr = input("Masukkan sebuah kalimat/kata : ")
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")
    
